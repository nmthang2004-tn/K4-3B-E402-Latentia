# CP4 — Hoàn thiện AI Spec & Khóa Quality Bar

> **Deadline:** 21:00 ngày 18/9
> **⛔ Sau 21:00 — Quality bar bị KHÓA, không sửa được**

---

## Mục tiêu CP4

1. **Hoàn thiện spec.md** — đủ §1–§9
2. **Khóa quality bar** — commit trước 21:00
3. **Git commit & push** — có timestamp

---

## Form CP4 — Câu trả lời

| Câu hỏi | Trả lời |
|-----------|----------|
| **Link spec.md trên GitHub** | [USER FILL - sau khi push] |
| **Chuẩn "đạt" của nhóm là gì?** | ✅ Đạt khi tổng thể ≥ 85% qua bộ kiểm thử, 100% case Lớp ① (No-Grounding) không được hallucinate/bịa đặt thông tin mà phải fallback chuyển TA, và 100% câu trả lời có căn cứ phải kèm trích dẫn nguồn. |
| **Phần nào chưa làm xong?** | - Discord bot với AI thật (Tuấn đang làm)<br>- Prompt templates cho 4 đường đi (Vàng đang làm)<br>- Kết quả chạy golden set trên AI thật (Run 2)<br>- Video 30 giây demo thật |

---

## Checklist spec.md §1–§9

### ✅ Đã hoàn thiện

| Mục | Nội dung | Status |
|------|----------|--------|
| §1 | Job executor, Core JTBD, Problem statement, Evidence (mining + survey) | ✅ |
| §2 | Bảng impact 3 ứng viên, lý do loại/chọn | ✅ |
| §3 | 2 giải pháp tương tự (ChatGPT, Bot hiện tại) | ✅ |
| §4 | Lát cắt 1 câu, Non-goals (4), Prototype level, Automation + cost-of-error, §4b (5 HAX/PAIR) | ✅ |
| §5 | 4 lớp + 10 kịch bản | ✅ |
| §6 | Sơ đồ 4 đường đi + mô tả chi tiết | ✅ |
| §7 | Chiều chất lượng, Golden set 24 cases, Quality bar | ✅ |
| §8 | Phân công 3 người, Willing users 3 người | ✅ |
| §9 | Changelog | ✅ |

### ⬜ Chưa hoàn thiện (tự khai)

| Mục | Nội dung | Ghi chú |
|------|----------|---------|
| eval/run-2-results.json | Kết quả chạy trên AI thật | Đang chờ Tuấn |
| Video demo | Video 30 giây | Đang chờ Tuấn |
| codebase/prompts/ | System prompt + templates | Đang chờ Vàng |

---

## Git Commands — Thực hiện đúng thứ tự

```bash
# 1. Commit spec.md
git add spec.md
git commit -m "docs: finalize spec.md and freeze quality bar for CP4"
git push origin main

# 2. Copy link spec.md trên GitHub
# Link dạng: https://github.com/[username]/[repo]/blob/main/spec.md
```

---

## ⛔ Lưu ý quan trọng

1. **Quality bar KHÓA sau 21:00** — không sửa được nữa
2. **Tự khai phần chưa xong** — không bị trừ điểm; giấu mới bị trừ
3. **Tiếp tục cập nhật bảng kết quả** ở §7 cho đến CP6

---

## Đáp án mẫu cho Form CP4

```
Link spec.md: https://github.com/[username]/K4-3B-E402-Latentia/blob/main/spec.md

Chuẩn "đạt": Đạt khi tổng thể ≥ 85% qua bộ kiểm thử, 100% case Lớp ① 
(No-Grounding) không được hallucinate/bịa đặt thông tin mà phải fallback 
chuyển TA, và 100% câu trả lời có căn cứ phải kèm trích dẫn nguồn.

Phần chưa xong: Discord bot với AI thật đang build (Tuấn), Prompt 
templates đang viết (Vàng), Run 2 trên AI thật và video demo 30 giây 
sẽ hoàn thành sau CP4.
```
