"""
Configuration management for Trợ lý Discord (K4-3B Latentia)
Tác giả: Nguyễn Minh Tuấn (2A202602420)
Mục đích: Đọc và quản lý biến môi trường, thiết lập API keys và đường dẫn hệ thống.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Base paths
CODEBASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CODEBASE_DIR.parent
EVAL_DIR = PROJECT_ROOT / "eval"
LOGS_DIR = CODEBASE_DIR / "logs"
PROMPTS_DIR = CODEBASE_DIR / "prompts"
MOCK_DATA_PATH = CODEBASE_DIR / "mock-data.json"

# Create logs directory if not exists
LOGS_DIR.mkdir(parents=True, exist_ok=True)

# Load .env file from codebase/.env or project root .env
dotenv_path = CODEBASE_DIR / ".env"
if not dotenv_path.exists():
    dotenv_path = PROJECT_ROOT / ".env"

if dotenv_path.exists():
    load_dotenv(dotenv_path=dotenv_path)
else:
    load_dotenv()  # Fallback to system environment

# Discord Bot Settings
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN", "").strip()
DISCORD_CHANNEL_ID = os.getenv("DISCORD_CHANNEL_ID", "").strip()
TA_ROLE_NAME = os.getenv("TA_ROLE_NAME", "@TA").strip()

# AI Provider Settings (Default: Google Gemini)
AI_PROVIDER = os.getenv("AI_PROVIDER", "gemini").strip().lower()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite").strip()
_gemini_fallback_raw = os.getenv(
    "GEMINI_FALLBACK_MODELS",
    "gemini-3.8-flash,gemini-3.7-flash,gemini-flash-latest",
)
GEMINI_FALLBACK_MODELS = [
    model.strip() for model in _gemini_fallback_raw.split(",") if model.strip()
]

# Backup Provider Settings (OpenAI)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "").strip()
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini").strip()

# Generation parameters
TEMPERATURE = float(os.getenv("AI_TEMPERATURE", "0.0"))  # 0.0 to strictly prevent hallucination
MAX_OUTPUT_TOKENS = int(os.getenv("AI_MAX_OUTPUT_TOKENS", "1000"))
THINKING_BUDGET = int(os.getenv("AI_THINKING_BUDGET", "0"))  # 0 = tắt thought tokens để tối ưu tốc độ và tránh cắt cụt câu trả lời
# Một số máy hackathon có proxy CA riêng; mặc định vẫn xác thực TLS.
AI_SSL_VERIFY = os.getenv("AI_SSL_VERIFY", "true").strip().lower() not in {"0", "false", "no"}
