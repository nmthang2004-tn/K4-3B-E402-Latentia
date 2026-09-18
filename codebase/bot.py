"""
Discord Bot Handler for Trợ lý Hỗ trợ Học viên (K4-3B Latentia)
Tác giả: Nguyễn Minh Tuấn (2A202602420)
Mục đích: Lắng nghe câu hỏi của học viên trên Discord, chuyển tiếp qua AI Client,
          phản hồi kèm trích dẫn nguồn hoặc kích hoạt Fallback hỗ trợ từ TA.
"""

import sys
import argparse
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Thêm đường dẫn project root vào sys.path để import an toàn
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from typing import Any, Optional

try:
    from codebase.config import DISCORD_BOT_TOKEN, DISCORD_CHANNEL_ID, TA_ROLE_NAME
    from codebase.ai_client import get_ai_assistant
    from codebase.logger import get_logger
except ImportError:
    from config import DISCORD_BOT_TOKEN, DISCORD_CHANNEL_ID, TA_ROLE_NAME  # type: ignore
    from ai_client import get_ai_assistant  # type: ignore
    from logger import get_logger  # type: ignore

logger = get_logger()

# Kiểm tra thư viện discord.py
try:
    import discord
    from discord.ext import commands
except ImportError as exc:
    print("❌ Lỗi: Thư viện discord.py chưa được cài đặt. Vui lòng chạy: pip install -r codebase/requirements.txt")
    sys.exit(1)


def create_bot():
    """Tạo và cấu hình Discord Client với Message Content Intents."""
    intents = discord.Intents.default()
    intents.message_content = True  # Yêu cầu để đọc nội dung tin nhắn học viên

    bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)
    ai = get_ai_assistant()

    @bot.event
    async def on_ready():
        logger.info(f"🤖 Bot đã đăng nhập thành công dưới tên: {bot.user} (ID: {getattr(bot.user, 'id', 'N/A')})")
        logger.info("Sẵn sàng hỗ trợ học viên lớp 3B.")
        # Cập nhật trạng thái hiển thị
        activity = discord.Activity(type=discord.ActivityType.listening, name="câu hỏi học viên | @mention")
        await bot.change_presence(activity=activity)

    @bot.event
    async def on_message(message: Any):
        # 1. Bỏ qua tin nhắn từ chính bot hoặc bot khác
        if getattr(message.author, "bot", False):
            return

        # 2. Kiểm tra kênh chỉ định (nếu có cấu hình DISCORD_CHANNEL_ID)
        if DISCORD_CHANNEL_ID and str(message.channel.id) != str(DISCORD_CHANNEL_ID):
            # Nếu không phải kênh chỉ định, chỉ trả lời khi được tag trực tiếp
            if not bot.user.mentioned_in(message):
                return

        # 3. Kiểm tra xem bot có được gọi không (mention hoặc direct chat hoặc lệnh !hoi)
        is_mentioned = bool(bot.user and (bot.user.mentioned_in(message) or bot.user in message.mentions))
        is_dm = isinstance(message.channel, discord.DMChannel)
        is_command = message.content.strip().startswith("!hoi") or message.content.strip().startswith("/hoi")

        if is_mentioned or is_dm or is_command or not DISCORD_CHANNEL_ID:
            # Lọc bỏ phần tag mention bot khỏi câu hỏi
            clean_question = message.clean_content
            if bot.user:
                clean_question = clean_question.replace(f"@{bot.user.name}", "")
                clean_question = clean_question.replace(f"@{bot.user.display_name}", "")
            if clean_question.startswith("!hoi"):
                clean_question = clean_question[4:]
            elif clean_question.startswith("/hoi"):
                clean_question = clean_question[4:]

            clean_question = clean_question.strip()
            if not clean_question:
                await message.reply(
                    "Xin chào! Mình là Trợ lý Discord lớp 3B. Bạn cần tra cứu thông tin gì về deadline, lịch trình hay quy chế lớp học?",
                    mention_author=False,
                )
                return

            # Hiển thị trạng thái đang soạn tin (typing)
            async with message.channel.typing():
                ai_result = ai.ask(clean_question)
                reply_text = ai_result.get("text", "Không nhận được câu trả lời.")

                # Fallback check: Nếu kết quả chuyển tiếp TA thì hỗ trợ tag TA rõ ràng
                if "@TA" in reply_text and TA_ROLE_NAME and TA_ROLE_NAME != "@TA":
                    reply_text = reply_text.replace("@TA", TA_ROLE_NAME)

                # Discord giới hạn tin nhắn 2000 ký tự
                if len(reply_text) > 1950:
                    reply_text = reply_text[:1950] + "...\n(Đã rút gọn)"

                await message.reply(reply_text, mention_author=False)

        await bot.process_commands(message)

    return bot


def run_cli_interactive():
    """Chế độ console tương tác trực tiếp giúp Tuấn test AI & flow mà không cần mở Discord."""
    print("=" * 60)
    print("🤖 CHẾ ĐỘ TEST TRỰC TIẾP TRỢ LÝ AI (CONSOLE TEST MODE)")
    print("Gõ câu hỏi để kiểm tra AI phản hồi, hoặc gõ 'exit' để thoát.")
    print("=" * 60)
    ai = get_ai_assistant()

    while True:
        try:
            user_input = input("\n[Học viên]: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["exit", "quit", "q"]:
                print("Tạm biệt!")
                break

            result = ai.ask(user_input)
            print(f"\n[Bot Phản hồi] (Latency: {result.get('latency', 0):.2f}s):")
            print(result.get("text", ""))
        except (KeyboardInterrupt, EOFError):
            break


def main():
    parser = argparse.ArgumentParser(description="Discord Bot & AI Assistant Runner")
    parser.add_argument("--test", type=str, help="Chạy test nhanh 1 câu hỏi cụ thể qua CLI")
    parser.add_argument("--interactive", action="store_true", help="Chạy chế độ console tương tác trực tiếp")
    args = parser.parse_args()

    if args.test:
        ai = get_ai_assistant()
        res = ai.ask(args.test)
        print(f"Query: {args.test}")
        print(f"Latency: {res.get('latency', 0):.2f}s")
        print(f"Response: {res.get('text')}")
        return

    if args.interactive:
        run_cli_interactive()
        return

    # Chạy Discord Bot thật
    if not DISCORD_BOT_TOKEN:
        print("Lỗi: DISCORD_BOT_TOKEN chưa được thiết lập trong .env!")
        print("Gợi ý: Copy file codebase/.env.example sang codebase/.env và điền Token của bạn.")
        print("Hoặc chạy thử nghiệm CLI bằng lệnh: python codebase/bot.py --interactive")
        sys.exit(1)

    bot = create_bot()
    if bot:
        bot.run(DISCORD_BOT_TOKEN)


if __name__ == "__main__":
    main()
