"""
AI Integration Client for Trợ lý Discord (K4-3B Latentia)
Tác giả: Nguyễn Minh Tuấn (2A202602420)
Mục đích: Tích hợp API mô hình AI thật (Google Gemini / OpenAI), nạp ngữ cảnh dữ liệu lớp học,
          và hỗ trợ cơ chế cắm Prompt linh hoạt (chờ dữ liệu hoàn thiện từ Vàng).
"""

import json
import sys
import time
from pathlib import Path
from typing import Any, Dict, Optional

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Đảm bảo đường dẫn project root và codebase luôn có trong sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
CODEBASE_DIR = Path(__file__).resolve().parent
if str(CODEBASE_DIR) not in sys.path:
    sys.path.insert(0, str(CODEBASE_DIR))

try:
    from codebase.config import (
        AI_PROVIDER,
        GEMINI_API_KEY,
        GEMINI_MODEL,
        MOCK_DATA_PATH,
        OPENAI_API_KEY,
        OPENAI_MODEL,
        PROMPTS_DIR,
        TEMPERATURE,
        MAX_OUTPUT_TOKENS,
        THINKING_BUDGET,
    )
    from codebase.logger import get_logger, log_interaction
except ImportError:
    from config import (  # type: ignore
        AI_PROVIDER,
        GEMINI_API_KEY,
        GEMINI_MODEL,
        MOCK_DATA_PATH,
        OPENAI_API_KEY,
        OPENAI_MODEL,
        PROMPTS_DIR,
        TEMPERATURE,
        MAX_OUTPUT_TOKENS,
        THINKING_BUDGET,
    )
    from logger import get_logger, log_interaction  # type: ignore

logger = get_logger()


class CourseAssistantAI:
    def __init__(self):
        self.provider = AI_PROVIDER
        self.gemini_client = None
        self.openai_client = None
        self.knowledge_context = self._load_knowledge_context()

        self._init_clients()

    def _init_clients(self):
        """Khởi tạo AI Client tương ứng dựa trên cấu hình."""
        if self.provider == "gemini" or not self.provider:
            if GEMINI_API_KEY:
                try:
                    from google import genai

                    self.gemini_client = genai.Client(api_key=GEMINI_API_KEY)
                    logger.info(f"Đã khởi tạo Gemini Client thành công với model: {GEMINI_MODEL}")
                except Exception as e:
                    logger.error(f"Không thể khởi tạo Gemini Client: {e}")
            else:
                logger.warning("GEMINI_API_KEY chưa được thiết lập trong .env")

        elif self.provider == "openai":
            if OPENAI_API_KEY:
                try:
                    from openai import OpenAI

                    self.openai_client = OpenAI(api_key=OPENAI_API_KEY)
                    logger.info(f"Đã khởi tạo OpenAI Client thành công với model: {OPENAI_MODEL}")
                except Exception as e:
                    logger.error(f"Không thể khởi tạo OpenAI Client: {e}")
            else:
                logger.warning("OPENAI_API_KEY chưa được thiết lập trong .env")

    def _load_knowledge_context(self) -> str:
        """Đọc và định dạng cơ sở dữ liệu tri thức từ mock-data.json làm CONTEXT_DATA."""
        if not MOCK_DATA_PATH.exists():
            return "Không có dữ liệu tri thức khóa học."

        try:
            with open(MOCK_DATA_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)

            context_lines = ["=== DỮ LIỆU THÔNG BÁO & QUY CHẾ CHÍNH THỨC CỦA LỚP 3B ==="]
            
            # 1. Knowledge Base (tài liệu thông báo, kênh nguồn)
            kb_list = data.get("knowledge_base", [])
            for item in kb_list:
                title = item.get("title", "")
                content = item.get("content", "")
                source = item.get("source", "")
                context_lines.append(f"• [{title}]: {content} (Nguồn: {source})")

            # 2. Key Deadlines
            deadlines = data.get("key_deadlines", [])
            if deadlines:
                context_lines.append("\n=== LỊCH TRÌNH & HẠN NỘP BÀI QUAN TRỌNG ===")
                for dl in deadlines:
                    context_lines.append(
                        f"• {dl.get('milestone')}: Hạn {dl.get('due_date')} lúc {dl.get('due_time')}. "
                        f"Kênh: {dl.get('channel')}. Ghi chú: {dl.get('notes', '')}"
                    )

            # 3. Schedule & Contact
            schedule = data.get("schedule", {})
            if schedule:
                standup = schedule.get("daily_standup", {})
                context_lines.append(
                    f"\n• Lịch Standup: {standup.get('time', '')} tại {standup.get('location', '')}. "
                    f"Thời lượng: {standup.get('duration_max', '')}. Nguồn: {standup.get('source', '')}"
                )

            return "\n".join(context_lines)
        except Exception as e:
            logger.error(f"Lỗi khi đọc mock-data.json: {e}")
            return "Lỗi nạp cơ sở tri thức."

    def get_system_prompt(self) -> str:
        """
        Đọc System Prompt:
        - Ưu tiên đọc từ codebase/prompts/system.md nếu file đã được bạn Vàng cung cấp.
        - Nếu chưa có, sử dụng Base Instruction an toàn (chống hallucination, bắt buộc trích dẫn nguồn, fallback chuyển TA).
        """
        system_file = PROMPTS_DIR / "system.md"
        if system_file.exists():
            try:
                with open(system_file, "r", encoding="utf-8") as f:
                    content = f.read().strip()
                    if content:
                        return content
            except Exception as e:
                logger.warning(f"Lỗi đọc prompt từ {system_file}: {e}")

        # Fallback base instruction (khi chưa có file chính thức từ Vàng)
        return (
            "Bạn là Trợ lý Discord hỗ trợ học viên lớp 3B (K4-3B Latentia).\n"
            "Nhiệm vụ: Trả lời ngắn gọn (<= 3 câu), chính xác các câu hỏi về lịch học, deadline, quy chế môn học.\n\n"
            "QUY TẮC BẮT BUỘC:\n"
            "1. CHỈ TRẢ LỜI dựa trên thông tin có trong [CONTEXT_DATA] được cung cấp. TUYỆT ĐỐI KHÔNG SUY ĐOÁN hay BỊA ĐẶT.\n"
            "2. BẮT BUỘC TRÍCH DẪN NGUỒN: Mọi câu trả lời đúng phải có dòng kết thúc dạng: 📌 Nguồn: [Kênh/Tài liệu].\n"
            "3. NẾU KHÔNG CÓ CĂN CỨ TRONG DỮ LIỆU (No-Grounding): Tuyệt đối không đoán ngày/giờ, phải trả lời nguyên văn: "
            "'Mình chưa tìm thấy thông tin này trong tài liệu thông báo. Bạn tag @TA để được hỗ trợ nhé!'\n"
            "4. NẾU CÂU HỎI MƠ HỒ (Low-Confidence): Đặt câu hỏi làm rõ ngắn gọn.\n"
            "5. NẾU NGOÀI PHẠM VI (giải bài tập, code hộ, tạo vote, điểm danh hộ): Lịch sự từ chối và nhắc hỏi đúng kênh."
        )

    def build_full_prompt(self, user_question: str) -> str:
        """Ghép câu hỏi của người dùng cùng với Context dữ liệu."""
        return (
            f"[CONTEXT_DATA]:\n"
            f"{self.knowledge_context}\n\n"
            f"[USER_QUESTION]:\n"
            f"{user_question}\n\n"
            f"[INSTRUCTION]:\n"
            f"Dựa vào [CONTEXT_DATA], hãy phản hồi câu hỏi của học viên tuân thủ nghiêm ngặt các quy tắc trên."
        )

    def ask(self, question: str) -> Dict[str, Any]:
        """
        Thực hiện gửi prompt và nhận phản hồi từ AI thật.
        Ghi log đầy đủ prompt -> response vào codebase/logs/.
        """
        start_time = time.time()
        system_instruction = self.get_system_prompt()
        full_prompt = self.build_full_prompt(question)

        # 1. Trường hợp dùng Google Gemini
        if self.provider == "gemini" and self.gemini_client:
            try:
                from google.genai import types

                gen_kwargs: Dict[str, Any] = {
                    "system_instruction": system_instruction,
                    "temperature": TEMPERATURE,
                    "max_output_tokens": MAX_OUTPUT_TOKENS,
                }
                if "lite" not in GEMINI_MODEL.lower() and hasattr(types, "ThinkingConfig"):
                    gen_kwargs["thinking_config"] = types.ThinkingConfig(thinking_budget=THINKING_BUDGET)

                config = types.GenerateContentConfig(**gen_kwargs)

                response = self.gemini_client.models.generate_content(
                    model=GEMINI_MODEL,
                    contents=full_prompt,
                    config=config,
                )
                
                reply_text = response.text.strip() if response.text else "Không nhận được phản hồi từ AI."
                latency = time.time() - start_time

                log_entry = log_interaction(
                    query=question,
                    prompt_sent=full_prompt,
                    response=reply_text,
                    latency_sec=latency,
                    provider="gemini",
                    model=GEMINI_MODEL,
                    success=True,
                )

                return {
                    "text": reply_text,
                    "latency": latency,
                    "provider": "gemini",
                    "model": GEMINI_MODEL,
                    "success": True,
                    "log_entry": log_entry,
                }
            except Exception as e:
                latency = time.time() - start_time
                error_msg = f"Lỗi gọi Gemini API: {e}"
                logger.error(error_msg)
                log_interaction(
                    query=question,
                    prompt_sent=full_prompt,
                    response=error_msg,
                    latency_sec=latency,
                    provider="gemini",
                    model=GEMINI_MODEL,
                    success=False,
                )
                return {
                    "text": f"⚠️ Có lỗi kết nối AI: {e}",
                    "latency": latency,
                    "provider": "gemini",
                    "model": GEMINI_MODEL,
                    "success": False,
                }

        # 2. Trường hợp dùng OpenAI (Dự phòng)
        elif self.provider == "openai" and self.openai_client:
            try:
                messages = [
                    {"role": "system", "content": system_instruction},
                    {"role": "user", "content": full_prompt},
                ]
                completion = self.openai_client.chat.completions.create(
                    model=OPENAI_MODEL,
                    messages=messages,
                    temperature=TEMPERATURE,
                    max_tokens=MAX_OUTPUT_TOKENS,
                )
                reply_text = completion.choices[0].message.content.strip()
                latency = time.time() - start_time

                log_entry = log_interaction(
                    query=question,
                    prompt_sent=full_prompt,
                    response=reply_text,
                    latency_sec=latency,
                    provider="openai",
                    model=OPENAI_MODEL,
                    success=True,
                )

                return {
                    "text": reply_text,
                    "latency": latency,
                    "provider": "openai",
                    "model": OPENAI_MODEL,
                    "success": True,
                    "log_entry": log_entry,
                }
            except Exception as e:
                latency = time.time() - start_time
                error_msg = f"Lỗi gọi OpenAI API: {e}"
                logger.error(error_msg)
                log_interaction(
                    query=question,
                    prompt_sent=full_prompt,
                    response=error_msg,
                    latency_sec=latency,
                    provider="openai",
                    model=OPENAI_MODEL,
                    success=False,
                )
                return {
                    "text": f"⚠️ Có lỗi kết nối OpenAI: {e}",
                    "latency": latency,
                    "provider": "openai",
                    "model": OPENAI_MODEL,
                    "success": False,
                }

        # 3. Trường hợp chưa cấu hình API Key trong .env
        latency = time.time() - start_time
        notice_text = (
            "⚠️ [AI Client] Chưa cấu hình GEMINI_API_KEY trong file codebase/.env.\n"
            "Vui lòng tạo file .env từ .env.example và điền API key để kích hoạt gọi AI thật."
        )
        log_interaction(
            query=question,
            prompt_sent=full_prompt,
            response=notice_text,
            latency_sec=latency,
            provider="none",
            model="none",
            success=False,
        )
        return {
            "text": notice_text,
            "latency": latency,
            "provider": "none",
            "model": "none",
            "success": False,
        }


# Singleton instance tiện cho việc import và tái sử dụng
_ai_assistant = None

def get_ai_assistant() -> CourseAssistantAI:
    global _ai_assistant
    if _ai_assistant is None:
        _ai_assistant = CourseAssistantAI()
    return _ai_assistant


if __name__ == "__main__":
    print("=" * 60)
    print("🤖 KIỂM TRA ĐỘC LẬP AI CLIENT (codebase/ai_client.py)")
    print("=" * 60)
    client = get_ai_assistant()
    test_query = "Hạn nộp Lab02 là khi nào?"
    print(f"Câu hỏi kiểm tra: {test_query}")
    result = client.ask(test_query)
    print(f"Kết quả (Latency: {result.get('latency', 0):.2f}s):")
    print(result.get("text"))
    print("=" * 60)
