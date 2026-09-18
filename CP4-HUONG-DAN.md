# CP4 — Hoàn thiện AI Spec & Khóa Quality Bar

> **Deadline:** 21:00 ngày 18/9
> **⛔ Sau 21:00 — Quality bar bị KHÓA, không sửa được**

---

## Mục tiêu CP4

1. **Hoàn thiện spec.md** — đủ §1–§9
2. **Khóa quality bar** — commit trước 21:00
3. **Git commit & push** — user tự làm

---

## Phân công CP4 (TUẦN TỰ)

### 🔴 THẮNG — Hoàn thiện spec.md (LÀM TRƯỚC)

> **Deadline cho Thắng: 20:30** (để Vàng + Tuấn còn thời gian)

**Nhiệm vụ:**
- [x] §1-§8 đã có trong spec.md ✅
- [x] Quality bar: "≥85%, 100% no-grounding không bịa, 100% trích dẫn" ✅
- [x] Cập nhật §9 Changelog (thêm dòng CP4) ✅
- [x] Kiểm tra đủ ≥5 nguyên tắc HAX/PAIR ✅ (5 nguyên tắc)
- [x] Kiểm tra đủ ≥8 kịch bản §5 ✅ (10 kịch bản)
- [x] Kiểm tra golden set link đúng ✅ (liên kết tương đối)

**Output:** spec.md sẵn sàng commit

---

### 🟡 VÀNG — Chuẩn bị prompts cho spec.md

> **Deadline cho Vàng: 20:45**

**Nhiệm vụ:**
- [x] Viết system prompt outline (đã hoàn thiện tại spec §4c & codebase/prompts/system.md) ✅
- [x] Viết prompt template cho 4 đường đi cốt lõi + 1 template Domain Policy (Happy, Low-conf, No-ground, Out-of-scope, Domain-policy tại codebase/prompts/templates/) ✅
- [x] Test thực nghiệm 5 cases Golden Set đạt 100% tại codebase/prompts/prompt_test_report.md ✅
- [x] Hoàn thiện báo cáo phân tích khảo sát n=14 học viên tại eval/survey_analysis.md ✅

---

### 🟢 TUẤN — Chuẩn bị prototype cho spec.md

> **Deadline cho Tuấn: 20:45**

**Nhiệm vụ:**
- [x] Kiểm tra codebase/ có AI call thật (dù chưa hoàn chỉnh) ✅ (`codebase/ai_client.py`, Run 2 và `codebase/logs/ai_interactions.jsonl`)
- [ ] Chuẩn bị 1-2 screenshot/video ngắn cho CP5
- [x] Ghi chú các chức năng đã có / chưa có ✅
  - Đã có: Gemini API call thật, prompt grounding, 4 nhánh xử lý, fallback model, logging prompt → response, runner 24 case.
  - Chưa có: screenshot/video CP5 và tích hợp Discord production hoàn chỉnh.

---

## Checklist spec.md §1–§9

### ✅ Đã hoàn thiện

| Mục | Nội dung | Status |
|------|----------|--------|
| §1 | Job executor, Core JTBD, Problem statement, Evidence | ✅ |
| §2 | Bảng impact 3 ứng viên, lý do loại/chọn | ✅ |
| §3 | 2 giải pháp tương tự | ✅ |
| §4 | Lát cắt, Non-goals, Automation, §4b HAX/PAIR | ✅ |
| §5 | 4 lớp + 10 kịch bản | ✅ |
| §6 | Sơ đồ 4 đường đi | ✅ |
| §7 | Chiều chất lượng, Golden set, Quality bar | ✅ |
| §8 | Phân công, Willing users | ✅ |

### ⬜ Cần kiểm tra / bổ sung

| Mục | Nội dung | Thắng check |
|------|----------|-------------|
| §4b | Đủ ≥4 HAX/PAIR + vị trí áp dụng | [x] ✅ |
| §5 | Đủ ≥8 kịch bản | [x] ✅ |
| §7 | Golden set link đúng | [x] ✅ |
| §9 | Changelog CP4 | [x] ✅ |

---

## Form CP4 — Điền khi Thắng xong

| Câu hỏi | Trả lời |
|-----------|----------|
| **Link spec.md trên GitHub** | https://github.com/nmthang2004-tn/K4-3B-E402-Latentia/blob/main/spec.md |
| **Chuẩn "đạt" của nhóm là gì?** | Đạt khi tổng thể ≥ 85% qua bộ kiểm thử, 100% case Lớp ① (No-Grounding) không được hallucinate/bịa đặt thông tin mà phải fallback chuyển TA, và 100% câu trả lời có căn cứ phải kèm trích dẫn nguồn. |
| **Phần nào chưa làm xong?** | Run 2 đã đạt 24/24 (100%), No-Grounding 100% và citation 100%. Video demo 30 giây/link public chưa có; Discord bot và phần tích hợp hoàn chỉnh vẫn do Tuấn phụ trách. |

---

## ⛔ Lưu ý quan trọng

1. **Thắng làm TRƯỚC** — để Vàng + Tuấn biết đường đi
2. **Quality bar KHÓA sau 21:00** — không sửa được
3. **Tự khai phần chưa xong** — không bị trừ điểm; giấu mới bị trừ
4. **Git do user tự commit** — không cần tôi làm
