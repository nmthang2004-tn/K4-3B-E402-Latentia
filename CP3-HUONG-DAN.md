# CP3 — Xây dựng Prototype AI thật & Đo lường kiểm thử

> **Deadline:** 16:00 ngày 18/9

---

## Mục tiêu CP3

1. **AI thật** — ít nhất 1 lời gọi mô hình AI tại mắt xích quyết định trung tâm
2. **Golden set** — đủ 20 case phân loại theo 4 lớp
3. **Đo lường** — chạy test, ghi kết quả, phân tích lỗi
4. **Video** — quay 30 giây demo thật

---

## Thứ tự làm việc (TUẦN TỰ)

### 🔴 Bước 1 — THẮNG (làm trước)

> Golden set phải xong trước để Vàng viết prompt, Tuấn build bot

- [x] **Golden set 24 cases** ✅ (đã có trong `eval/`)
- [x] **Quality bar** ✅ (≥85%, 100% no-grounding không bịa, 100% trích dẫn)
- [x] Tạo script **run_eval.py** để chạy golden set tự động ✅
- [x] Viết **analysis.md** — phân tích lỗi Run 2 (`eval/analysis.md`) ✅

**Output cho bước tiếp theo:** `eval/golden_set.json`, `eval/run_eval.py`

---

### 🟡 Bước 2 — VÀNG (sau khi Thắng xong)

> Prompt phải xong trước để Tuấn tích hợp vào bot

- [x] Viết **system prompt** cho bot (role, phạm vi, cách trả lời) ✅ (`codebase/prompts/system.md`)
- [x] Viết **prompt templates** cho từng đường đi: ✅ (`codebase/prompts/templates/`)
  - Happy path: có căn cứ → trả lời + trích dẫn
  - Low-confidence: mơ hồ → hỏi làm rõ
  - No-grounding: không tìm thấy → chuyển TA
  - Out-of-scope: ngoài phạm vi → từ chối
  - Domain policy: quy chế đặc thù
- [x] Test prompt với 5 cases trong golden set ✅ (`codebase/prompts/test_prompts_5cases.py`)
- [x] Tinh chỉnh prompt dựa trên kết quả ✅ (`codebase/prompts/prompt_test_report.md`)

**Output cho bước tiếp theo:** `codebase/prompts/system.md`, `codebase/prompts/templates/` ✅ (Đã bàn giao cho Tuấn)

---

### 🟢 Bước 3 — TUẤN (sau khi Vàng xong)

> Build bot, chạy eval, quay video

- [ ] Xây dựng **Discord bot** với:
  - AI integration (Gemini/OpenAI)
  - Prompt từ Vàng
  - 4 đường đi xử lý
- [ ] Setup **logging** (prompt → response)
- [ ] Chạy **golden set 24 cases** qua bot
- [ ] Ghi kết quả vào `eval/run-2-results.json`
- [ ] Quay **video 30 giây** demo AI thật
- [ ] Upload video lên YouTube/Drive (public)

**Output:** `codebase/` (working bot), `eval/run-2-results.json`, video link

---

## Yêu cầu bắt buộc

### Codebase/ — Prototype AI thật

```
codebase/
├── bot.py              # Discord bot handler
├── ai_client.py        # AI API integration (Gemini)
├── prompts/            # System prompts từ Vàng
│   ├── system.md      # System prompt chính
│   └── templates/     # Prompt templates cho từng đường đi
├── logs/              # Prompt/response logs
├── config.py          # API keys, settings
├── .env.example       # Template for .env
└── run_eval.py       # Script chạy eval từ Thắng
```

### eval/ — Golden Set 24 cases

```
eval/
├── golden_set.json     # 24 test cases (Thắng đã làm)
├── run_eval.py        # Script chạy eval (Thắng làm)
├── run-1-results.json # Baseline (Thắng chạy)
├── run-2-results.json # Kết quả CP3 (Tuấn chạy)
└── analysis.md        # Phân tích lỗi (Thắng viết)
```

### Quality Bar

> *"Đạt khi tổng thể ≥ 85% qua bộ kiểm thử, 100% case Lớp ① (No-Grounding) không được hallucinate/bịa đặt thông tin mà phải fallback chuyển TA, và 100% câu trả lời có căn cứ phải kèm trích dẫn nguồn."*

---

## Form CP3 — Điền khi xong

| Câu hỏi | Trả lời |
|----------|----------|
| Link video thao tác 30 giây? | [USER FILL - YouTube/Drive public] |
| Đã thử bao nhiêu lần? | **24 lần** (golden set đầy đủ) |
| Trong đó bao nhiêu lần đạt? | **24/24 (100%)** |
| Chuẩn "đạt" của nhóm là gì? | ≥85% tổng thể + 100% Lớp ① không bịa + 100% có căn cứ phải trích dẫn |
| Những lần chưa đạt sai ở đâu? | Lượt đầu 11/24 do thiếu dữ kiện bắt buộc, wording nhánh out-of-scope và quota 15 request/phút; sau khi sửa prompt/runner, Run 2 chính thức đạt 24/24. Chi tiết tại `eval/analysis.md`. |

---

## Checklist CP3 (theo thứ tự)

### ✅ Thắng — Đã xong
- [x] Golden set 24 cases
- [x] Quality bar
- [x] Runner và phân tích lỗi (`eval/run_eval.py`, `eval/analysis.md`)

### ✅ Vàng — Đã xong
- [x] System prompt (`codebase/prompts/system.md`)
- [x] Prompt templates (`codebase/prompts/templates/`)
- [x] Thử nghiệm 5 cases & báo cáo tinh chỉnh (`codebase/prompts/prompt_test_report.md`)

### ⬜ Tuấn — Làm cuối
- [ ] Discord bot với AI
- [ ] Logging
- [ ] Chạy golden set
- [ ] Video 30 giây

---

## Lưu ý quan trọng

1. **Thứ tự bắt buộc:** Thắng → Vàng → Tuấn
2. **Nguyên tắc trung thực:** Khai đúng số liệu, kể cả khi fail nhiều
3. **AI thật bắt buộc:** Không hardcode response
4. **Logging bắt buộc:** Prompt input → AI response output phải được log
