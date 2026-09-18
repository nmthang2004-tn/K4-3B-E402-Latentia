"""
Interaction & AI Call Logger for Trợ lý Discord (K4-3B Latentia)
Tác giả: Nguyễn Minh Tuấn (2A202602420)
Mục đích: Ghi nhận minh bạch mọi lượt gọi prompt -> response, latency, metadata phục vụ đo lường kiểm thử CP3.
"""

import json
import logging
from datetime import datetime
from pathlib import Path
import sys
from pathlib import Path
from typing import Any, Dict, Optional

# Đảm bảo đường dẫn project root và codebase luôn có trong sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
CODEBASE_DIR = Path(__file__).resolve().parent
if str(CODEBASE_DIR) not in sys.path:
    sys.path.insert(0, str(CODEBASE_DIR))

try:
    from codebase.config import LOGS_DIR
except ImportError:
    from config import LOGS_DIR  # type: ignore

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

LOGS_DIR.mkdir(parents=True, exist_ok=True)
JSONL_LOG_PATH = LOGS_DIR / "ai_interactions.jsonl"
TEXT_LOG_PATH = LOGS_DIR / "bot.log"

# Setup standard python logger for console & text log file
_text_logger = logging.getLogger("CourseAssistantBot")
_text_logger.setLevel(logging.INFO)

if not _text_logger.handlers:
    # File handler
    file_handler = logging.FileHandler(TEXT_LOG_PATH, encoding="utf-8")
    file_handler.setLevel(logging.INFO)
    file_formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(file_formatter)
    _text_logger.addHandler(file_handler)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter("[%(levelname)s] %(message)s")
    console_handler.setFormatter(console_formatter)
    _text_logger.addHandler(console_handler)


def log_interaction(
    query: str,
    prompt_sent: str,
    response: str,
    latency_sec: float,
    provider: str = "gemini",
    model: str = "gemini-3.5-flash-lite",
    success: bool = True,
    metadata: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Ghi nhận chi tiết một phiên tương tác với AI vào file JSON Lines và file text log.
    Đáp ứng yêu cầu bắt buộc của CP3: logging (prompt -> response).
    """
    entry = {
        "timestamp": datetime.now().isoformat(),
        "query": query,
        "prompt_sent": prompt_sent,
        "response": response,
        "latency_sec": round(latency_sec, 3),
        "provider": provider,
        "model": model,
        "success": success,
        "metadata": metadata or {},
    }

    # 1. Ghi vào JSONL file (máy đọc, phục vụ phân tích / run eval)
    try:
        with open(JSONL_LOG_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    except Exception as e:
        _text_logger.error(f"Failed to write to {JSONL_LOG_PATH}: {e}")

    # 2. Ghi tóm tắt vào log text
    status_str = "SUCCESS" if success else "FAILED"
    _text_logger.info(
        f"[{status_str}] [{provider}/{model}] Latency: {entry['latency_sec']}s | "
        f"Query: \"{query[:40]}\" -> Response: \"{response[:60]}...\""
    )

    return entry


def get_logger() -> logging.Logger:
    return _text_logger
