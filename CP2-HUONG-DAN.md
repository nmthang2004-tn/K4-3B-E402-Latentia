# CP2 — Thiết kế luồng & Bản mẫu tương tác

> **Deadline:** 21:00 ngày 17/9

---

## Mục tiêu
Phát hiện lỗ hổng trải nghiệm và bất cập logic **trước** khi lập trình. Sửa sai trên sơ đồ tốn vài phút; sửa sau khi code xong tốn cả buổi trong sự kiện 39 giờ.

---

## Ba hình thức nộp (chọn 1)

| Hình thức | Công cụ gợi ý | Độ chi tiết |
|-----------|---------------|------------|
| Clickable prototype | Figma, Canva, HTML/CSS/JS | Cao — user bấm được |
| Sơ đồ luồng | Draw.io, Lucidchart, vẽ tay | Trung — thể hiện logic |
| Video quay màn hình | Quay 1 vòng từ đầu vào → kết quả cuối | Thấp — demo nhanh |

---

## Bốn đường đi cần thể hiện

1. **Happy path** — AI tự tin cao, trả lời được có trích dẫn
2. **Low-confidence (②)** — AI nghi ngờ, hỏi làm rõ trước khi trả lời
3. **No-grounding (①)** — Không tìm thấy căn cứ, chuyển TA
4. **Correction** — User sửa/tranh thán kết quả AI

---

## Bốn nguyên tắc HAX/PAIR bắt buộc

- **G10** (bắt buộc): Thu hẹp phạm vi khi nghi ngờ
- **G8** hoặc **G9**: Gạt bỏ / sửa dễ dàng
- **G11**: Giải thích vì sao
- +1 nguyên tắc tự chọn

---

## Cấp độ tự động hóa (cost-of-error)

| Mức | Khi nào dùng | Ví dụ |
|-----|-------------|-------|
| **Automate** | Sai thì rẻ, user tự sửa được | Gợi ý cú pháp code |
| **Conditional** | Đa số case lành, số ít hiểm | Trả lời có căn cứ → OK; không → chuyển TA |
| **Augment** | Sai thì đắt, cần người duyệt | Quiz do AI sinh |

→ Sản phẩm này: **Conditional**

---

## Phân công CP2

### 🟡 Nguyễn Minh Thắng — Product Lead ✅ ĐÃ LÀM

**Nhiệm vụ:** ✅ ĐÃ HOÀN THÀNH
- [x] Thiết kế 4 đường đi (happy path, low-confidence, no-grounding, correction)
- [x] Vẽ sơ đồ luồng (Mermaid diagram trong `codebase/flow-diagram.md`)
- [x] Cập nhật §4, §5, §6 trong spec.md (prototype level, nguyên tắc HAX/PAIR, 4 lớp lỗi)
- [x] Đảm bảo logic flow không có lỗ hổng

**Output:** `spec.md` (đã cập nhật) + `codebase/flow-diagram.md` ✅

---

### 🔵 Nguyễn Thị Vàng — Prompt/UX ✅ ĐÃ HOÀN THÀNH

**Nhiệm vụ:** ✅ ĐÃ HOÀN THÀNH
- [x] Thiết kế **conversation flow** (các tin nhắn mẫu cho từng nhánh trong `codebase/prompt-templates.md`) ✅
- [x] Viết **prompt template** cho mỗi trường hợp (có căn cứ, thiếu căn cứ, low-confidence, out-of-scope, domain-rule) ✅
- [x] Chuẩn bị **mock data** cho prototype (`codebase/mock-data.json` gồm 6 documents & 7 scenarios) ✅
- [x] Xây **Golden Set 24 cases** (vượt chuẩn ≥20 cases, lưu tại `eval/golden_set.json` & `eval/golden_set.md`, runner `eval/run_eval.py` test đạt 100% 24/24) ✅

**Output:** `codebase/prompt-templates.md` + `codebase/mock-data.json` + `eval/golden_set.json` + `eval/golden_set.md` + `eval/run_eval.py` ✅

---

### 🟢 Nguyễn Minh Tuấn — Build Prototype ✅ ĐÃ HOÀN THÀNH

**Nhiệm vụ:** ✅ ĐÃ HOÀN THÀNH
- [x] Dựng **clickable prototype** (HTML/JS) thể hiện 4 đường đi ✅
- [x] Sử dụng mock data chuẩn bị sẵn để demo tương tác ✅
- [x] Đã lưu vào `codebase/prototype/index.html` ✅
- [x] Đảm bảo prototype có thể click qua lại giữa 4 nhánh và edge cases không dead-end ✅
- [x] Kiểm thử toàn bộ flow tương tác và cơ chế HAX/PAIR (G1, G8, G9, G10, G11) ✅

**Output:** `codebase/prototype/index.html` + `codebase/mock-data.json` ✅

---

## Checklist trước khi nộp

- [x] Sơ đồ luồng thể hiện đủ 4 đường đi (`codebase/flow-diagram.md`) ✅
- [x] Prototype clickable tương tác mượt mà (`codebase/prototype/index.html`) ✅
- [x] §4, §5, §6 trong spec.md đã cập nhật đầy đủ ✅
- [x] Bảng nguyên tắc HAX/PAIR có đủ 4 nguyên tắc + vị trí áp dụng cụ thể ✅
- [x] Mock data sẵn sàng cho CP3 (`codebase/mock-data.json`) ✅
- [x] Golden Set 24 cases vượt chuẩn ≥20 cases (`eval/golden_set.json`) ✅
- [x] Chạy kiểm thử tự động đạt 100% (24/24 passed tại `eval/results/eval_run_cp2.json`) ✅
- [x] Không có dead-end trên bất kỳ nhánh nào ✅

---

## Hướng dẫn chi tiết từng bước

### Bước 1: Sơ đồ luồng (Thắng) ✅ ĐÃ LÀM

```
Đã hoàn thành:
- Sơ đồ Mermaid trong codebase/flow-diagram.md
- Cập nhật spec.md §4, §5, §6
```

### Bước 2: Prompt templates + Mock data (Vàng) ✅ ĐÃ LÀM

```
Đã hoàn thành:
- Prompt templates 4 nhánh + edge cases trong codebase/prompt-templates.md
- Mock data 6 docs và 7 scenarios trong codebase/mock-data.json
- Golden Set 24 cases test pass 100% trong eval/
```

### Bước 3: Build prototype (Tuấn) ✅ ĐÃ LÀM

```
Đã hoàn thành:
- Clickable prototype hoàn thiện trong codebase/prototype/index.html
- Giao diện Discord Dark Theme, mô phỏng phản hồi thật
- 4 đường đi cốt lõi + 2 edge cases không dead-end
```

### Bước 4: Test flow (Tuấn) ✅ ĐÃ HOÀN THÀNH

```
1. Đi hết 4 đường đi trên prototype: Đã kiểm tra trơn tru (Happy, Low-Conf, No-Grounding, Correction) ✅
2. Kiểm tra không có dead-end: Toàn bộ nút Sửa (G9), Bỏ qua (G8), Tag @TA đều chuyển trạng thái hợp lý ✅
3. Demo sẵn sàng trình chiếu trực tiếp hoặc quay video ✅
```

---

## Lưu ý quan trọng

1. **Mock data được** — không cần data thật, miễn là thể hiện đúng flow (Đã chuẩn hóa 100%)
2. **4 đường đi bắt buộc** — thiếu 1 bị trừ điểm (Đã có đủ 4/4 + 2 edge cases)
3. **Nguyên tắc HAX/PAIR** — mỗi nguyên tắc phải chỉ ra **vị trí cụ thể** trong prototype (Đã tích hợp vào drawer bên phải)
4. **Lưu vào codebase/** — tất cả artifact lưu vào thư mục codebase/ (Đã lưu đầy đủ)
