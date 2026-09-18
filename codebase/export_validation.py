"""
Trích xuất dữ liệu thực tế từ codebase/logs/ai_interactions.jsonl
vào thư mục validation/ phục vụ mốc CP5 & Rubric R6.
"""

import json
import sys
from datetime import datetime
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_FILE = BASE_DIR / "codebase" / "logs" / "ai_interactions.jsonl"
OUTPUT_DIR = BASE_DIR / "validation"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_RAW_JSON = OUTPUT_DIR / "live_test_interactions.json"

def main():
    if not LOG_FILE.exists():
        print(f"Không tìm thấy file log: {LOG_FILE}")
        return

    interactions = []
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                data = json.loads(line)
                interactions.append(data)
            except Exception:
                continue

    # Lọc các tương tác từ đợt test 19:00 ngày 18/9/2026
    test_run = [item for item in interactions if "2026-09-18T19:" in item.get("timestamp", "")]
    if not test_run:
        # Lấy 10 tương tác gần nhất nếu không khớp giờ
        test_run = interactions[-10:] if len(interactions) >= 10 else interactions

    print(f"Tổng số lượt tương tác trích xuất: {len(test_run)}")
    for i, item in enumerate(test_run, 1):
        print(f"\n[{i}] Query: {item.get('query')}")
        print(f"    Latency: {item.get('latency_sec')}s | Model: {item.get('model')}")
        print(f"    Response: {item.get('response')[:100]}...")

    with open(OUTPUT_RAW_JSON, "w", encoding="utf-8") as f:
        json.dump(test_run, f, ensure_ascii=False, indent=2)

    print(f"\n Đã lưu dữ liệu thô vào: {OUTPUT_RAW_JSON}")

if __name__ == "__main__":
    main()
