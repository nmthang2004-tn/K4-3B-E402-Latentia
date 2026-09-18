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
- [ ] Cập nhật §9 Changelog (thêm dòng CP4)
- [ ] Kiểm tra đủ ≥5 nguyên tắc HAX/PAIR
- [ ] Kiểm tra đủ ≥8 kịch bản §5
- [ ] Kiểm tra golden set link đúng

**Output:** spec.md sẵn sàng commit

---

### 🟡 VÀNG — Chuẩn bị prompts cho spec.md

> **Deadline cho Vàng: 20:45**

**Nhiệm vụ:**
- [x] Viết system prompt outline (đã hoàn thiện tại spec §4c & codebase/prompts/system.md) ✅
- [x] Viết prompt template cho 4 đường đi (Happy, Low-conf, No-ground, Out-of-scope tại codebase/prompts/templates/) ✅
- [x] Test thực nghiệm 5 cases Golden Set đạt 100% tại codebase/prompts/prompt_test_report.md ✅

---

### 🟢 TUẤN — Chuẩn bị prototype cho spec.md

> **Deadline cho Tuấn: 20:45**

**Nhiệm vụ:**
- [ ] Kiểm tra codebase/ có AI call thật (dù chưa hoàn chỉnh)
- [ ] Chuẩn bị 1-2 screenshot/video ngắn cho CP5
- [ ] Ghi chú các chức năng đã có / chưa có

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
| §4b | Đủ ≥4 HAX/PAIR + vị trí áp dụng | [ ] |
| §5 | Đủ ≥8 kịch bản | [x] ✅ |
| §7 | Golden set link đúng | [ ] |
| §9 | Changelog CP4 | [ ] |

---

## Form CP4 — Điền khi Thắng xong

| Câu hỏi | Trả lời |
|-----------|----------|
| **Link spec.md trên GitHub** | [USER FILL - sau khi push] |
| **Chuẩn "đạt" của nhóm là gì?** | Đạt khi tổng thể ≥ 85% qua bộ kiểm thử, 100% case Lớp ① (No-Grounding) không được hallucinate/bịa đặt thông tin mà phải fallback chuyển TA, và 100% câu trả lời có căn cứ phải kèm trích dẫn nguồn. |
| **Phần nào chưa làm xong?** | Discord bot đang build (Tuấn), Run 2 và video sẽ hoàn thành sau CP4 (System prompts và Prompt templates của Vàng đã hoàn thành 100%). |

---

## ⛔ Lưu ý quan trọng

1. **Thắng làm TRƯỚC** — để Vàng + Tuấn biết đường đi
2. **Quality bar KHÓA sau 21:00** — không sửa được
3. **Tự khai phần chưa xong** — không bị trừ điểm; giấu mới bị trừ
4. **Git do user tự commit** — không cần tôi làm
