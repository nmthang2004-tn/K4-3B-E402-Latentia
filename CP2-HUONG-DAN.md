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

### 🟡 Nguyễn Minh Thắng — Product Lead

**Nhiệm vụ:**
- Thiết kế **4 đường đi** (happy path, low-confidence, no-grounding, correction)
- Vẽ **sơ đồ luồng** tổng quan (dùng Draw.io/Lucidchart)
- Cập nhật **§4 và §6** trong spec.md (mức prototype, bảng nguyên tắc HAX/PAIR)
- Đảm bảo logic flow không có lỗ hổng

**Output:** `codebase/flow-diagram.png` + cập nhật spec.md

---

### 🔵 Nguyễn Thị Vàng — Prompt/UX

**Nhiệm vụ:**
- Thiết kế **conversation flow** (các tin nhắn mẫu cho từng nhánh)
- Viết **prompt template** cho mỗi trường hợp (có căn cứ, thiếu căn cứ, low-confidence)
- Chuẩn bị **mock data** cho prototype (câu hỏi mẫu + câu trả lời kỳ vọng)
- Đề xuất **4 nguyên tắc HAX/PAIR** kèm vị trí áp dụng trong prototype

**Output:** `codebase/prompt-templates.md` + `codebase/mock-data.json`

---

### 🟢 Nguyễn Minh Tuấn — Build Prototype

**Nhiệm vụ:**
- Dựng **clickable prototype** (Figma/HTML) thể hiện 4 đường đi
- Sử dụng mock data từ Vàng để demo
- Nếu dùng HTML: lưu vào `codebase/prototype/`
- Đảm bảo prototype có thể click qua lại giữa các nhánh

**Output:** `codebase/prototype/index.html` (hoặc link Figma)

---

## Checklist trước khi nộp

- [ ] Sơ đồ luồng thể hiện đủ 4 đường đi
- [ ] Prototype clickable hoặc video demo
- [ ] §4 và §6 trong spec.md đã cập nhật
- [ ] Bảng nguyên tắc HAX/PAIR có đủ 4 nguyên tắc + vị trí áp dụng
- [ ] Mock data sẵn sàng cho CP3

---

## Hướng dẫn chi tiết từng bước

### Bước 1: Vẽ sơ đồ luồng (Thắng)

```
1. Mở Draw.io hoặc Lucidchart
2. Vẽ các node:
   - Node bắt đầu: User gõ câu hỏi
   - Node AI xử lý: Tìm căn cứ trong tài liệu
   - Node quyết định: Có tìm thấy căn cứ?
     - Có → Node trả lời (Happy path)
     - Không → Node low-confidence (hỏi làm rõ)
   - Node quyết định 2: Có đủ căn cứ sau khi làm rõ?
     - Có → Node trả lời
     - Không → Node chuyển TA
3. Thêm node correction: User click "Sửa" / "Thử lại"
```

### Bước 2: Viết prompt templates (Vàng)

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

### Bước 3: Mock data (Vàng)

```json
[
  {
    "câu_hỏi": "Hạn nộp Lab02 là khi nào?",
    "kỳ_vọng": "Happy path - trả lời có trích dẫn"
  },
  {
    "câu_hỏi": "Deadline project cuối kỳ năm nay có thay đổi không?",
    "kỳ_vọng": "No-grounding - chuyển TA"
  },
  {
    "câu_hỏi": "Khi nào nộp?",
    "kỳ_vọng": "Low-confidence - hỏi làm rõ"
  }
]
```

### Bước 4: Build prototype (Tuấn)

**Option A: Figma**
1. Tạo frame cho mỗi màn hình (input, xử lý, output)
2. Thêm hotzone clickable để chuyển giữa các frame
3. Share link prototype

**Option B: HTML đơn giản**
1. Tạo `codebase/prototype/index.html`
2. Dùng mock data từ Vàng
3. JavaScript đơn giản để simulate các nhánh

---

## Lưu ý quan trọng

1. **Mock data được** — không cần data thật, miễn là thể hiện đúng flow
2. **4 đường đi bắt buộc** — thiếu 1 bị trừ điểm
3. **Nguyên tắc HAX/PAIR** — mỗi nguyên tắc phải chỉ ra **vị trí cụ thể** trong prototype
4. **Lưu vào codebase/** — tất cả artifact lưu vào thư mục codebase/
