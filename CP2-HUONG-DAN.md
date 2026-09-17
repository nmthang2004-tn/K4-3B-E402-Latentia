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

### 🔵 Nguyễn Thị Vàng — Prompt/UX

**Nhiệm vụ:**
- [ ] Thiết kế **conversation flow** (các tin nhắn mẫu cho từng nhánh)
- [ ] Viết **prompt template** cho mỗi trường hợp (có căn cứ, thiếu căn cứ, low-confidence)
- [ ] Chuẩn bị **mock data** cho prototype (câu hỏi mẫu + câu trả lời kỳ vọng)
- [ ] Xây **Golden Set ≥20 cases** (đã có 10 trong spec.md, cần thêm 10)

**Output:** `codebase/prompt-templates.md` + `codebase/mock-data.json`

---

### 🟢 Nguyễn Minh Tuấn — Build Prototype ✅ ĐÃ HOÀN THÀNH

**Nhiệm vụ:**
- [x] Dựng **clickable prototype** (HTML/JS) thể hiện 4 đường đi ✅
- [x] Sử dụng mock data chuẩn bị sẵn để demo tương tác ✅
- [x] Đã lưu vào `codebase/prototype/index.html` ✅
- [x] Đảm bảo prototype có thể click qua lại giữa 4 nhánh và edge cases không dead-end ✅

**Output:** `codebase/prototype/index.html` + `codebase/mock-data.json` ✅

---

## Checklist trước khi nộp

- [x] Sơ đồ luồng thể hiện đủ 4 đường đi ✅
- [x] Prototype clickable hoặc video demo (`codebase/prototype/index.html`) ✅
- [x] §4 và §6 trong spec.md đã cập nhật ✅
- [x] Bảng nguyên tắc HAX/PAIR có đủ 4 nguyên tắc + vị trí áp dụng ✅
- [x] Mock data sẵn sàng cho CP3 (`codebase/mock-data.json`) ✅

---

## Hướng dẫn chi tiết từng bước

### Bước 1: Sơ đồ luồng (Thắng) ✅ ĐÃ LÀM

```
Đã hoàn thành:
- Sơ đồ Mermaid trong codebase/flow-diagram.md
- Cập nhật spec.md §4, §5, §6
```

### Bước 2: Prompt templates + Mock data (Vàng)

```
Template 1: Happy path
- Input: Câu hỏi user về deadline/lịch
- Xử lý: Tìm trong tài liệu → Trích dẫn nguồn
- Output: "Theo thông báo ngày XX, deadline Lab02 là..."

Template 2: No-grounding
- Input: Câu hỏi không có trong tài liệu
- Xử lý: Không tìm thấy căn cứ
- Output: "Mình chưa tìm thấy thông tin này trong tài liệu. Bạn hỏi TA nhé: @TA"

Template 3: Low-confidence
- Input: Câu hỏi mơ hồ, thiếu thông tin
- Xử lý: Cần làm rõ
- Output: "Bạn đang hỏi về deadline nộp bài nào? Lab hay Project?"
```

### Bước 3: Build prototype (Tuấn)

```
1. Chọn tool: Figma (nhanh) hoặc HTML/JS (linh hoạt hơn)

2. Thiết kế màn hình:
   - Discord chat mockup với message thread
   - Bot response với action buttons
   - Các nhánh xử lý (clickable)

3. Demo 4 đường đi:
   - Happy path: đầy đủ thông tin → trả lời
   - Low-confidence: thông tin mơ hồ → hỏi làm rõ
   - No-grounding: không tìm thấy → chuyển TA
   - Correction: nút Sửa / Tag TA
```

### Bước 4: Test flow (Tuấn)

```
1. Đi hết 4 đường đi trên prototype
2. Kiểm tra không có dead-end
3. Quay video demo 30 giây
```

---

## Lưu ý quan trọng

1. **Mock data được** — không cần data thật, miễn là thể hiện đúng flow
2. **4 đường đi bắt buộc** — thiếu 1 bị trừ điểm
3. **Nguyên tắc HAX/PAIR** — mỗi nguyên tắc phải chỉ ra **vị trí cụ thể** trong prototype
4. **Lưu vào codebase/** — tất cả artifact lưu vào thư mục codebase/
