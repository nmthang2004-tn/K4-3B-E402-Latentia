# Validation Log — Nhóm Latentia (K4-3B-E402)

> **Người thực hiện:** Nguyễn Thị Vàng (2A202602897) — Prompt/UX & Eval Lead  
> **Dự án:** Trợ lý Discord hỗ trợ học viên · Track B1  
> **Thời gian thực hiện:** 18/09/2026 (Phiên 10 phút/người theo chuẩn §4.2 `02-guide.md`)  
> **Mục tiêu:** Kiểm chứng prototype AI thật với ≥3 willing users ngoài nhóm đã cam kết từ CP1, ghi nhận hành vi thực tế, trích xuất quote nguyên văn và tổng hợp các điều chỉnh thiết kế.

---

## 1. Nhật ký phiên kiểm thử người dùng (Validation Sessions)

### Người 1: Bùi Việt Anh — Học viên K4 lớp 3B (Willing User 1)
- **Task giao:** "Bạn hãy dùng bot trên Discord để tìm xem deadline nộp bài Lab 02 là khi nào và kiểm tra xem thông tin đó có đáng tin cậy không."
- **Thời gian hoàn thành:** 42 giây
- **Hành vi quan sát:**
  - Gõ lệnh: `@Trợ lý Hạn nộp Lab02 là khi nào?`
  - Đọc phản hồi trong 3 giây, mắt dừng lại ngay dòng `📌 Nguồn: #thong-bao-khoa-hoc (15/09/2026)`.
  - Nhấp chuột kiểm tra kênh `#thong-bao-khoa-hoc` để đối chiếu ngày 20/9.
  - Biểu cảm thở phào nhẹ nhõm, không cần cuộn ngược danh sách tin ghim (pinned messages) như mọi khi.
  - Thử rê chuột vào các gợi ý thao tác bên dưới câu trả lời.
- **Quote nguyên văn:**
  > *"Bot trả lời thẳng vào ngày giờ nộp kèm link kênh thông báo nên rất an tâm, không sợ bị troll hay nhầm hạn cũ như trước."*
- **Điểm kẹt:** Người dùng ban đầu hơi khựng lại 2 giây vì phân vân không biết gõ tên bài là `Lab02`, `Lab 02` hay `lab 2` thì bot có nhận diện được không.
- **Quyết định thay đổi:** Giữ nguyên prompt xử lý regex/fuzzy case-insensitive; bổ sung câu hướng dẫn ngắn ở tin nhắn chào (`G1`) để học viên biết có thể gõ tự nhiên không cần chuẩn cú pháp.

---

### Người 2: Hà Anh Tuấn — Học viên K4 lớp 3B (Willing User 2)
- **Task giao:** "Giả sử bạn chỉ nhớ mang máng là sắp phải nộp một bài gì đó, hãy hỏi bot xem khi nào nộp và xử lý tiếp theo phản hồi của bot."
- **Thời gian hoàn thành:** 1 phút 15 giây
- **Hành vi quan sát:**
  - Gõ câu hỏi mơ hồ: `@Trợ lý Khi nào nộp bài?`
  - Quan sát phản hồi của bot: Bot không đoán mò mà kích hoạt kịch bản Low-confidence (HAX G10), hỏi lại: *"Bạn đang hỏi về hạn nộp Lab 02 (hạn 20/9) hay Milestone 1 Project (hạn 25/9)?"*
  - Người dùng mỉm cười, gõ phản hồi: `Lab 02`.
  - Bot trả về ngay kết quả chính xác kèm trích dẫn nguồn kênh thông báo.
- **Quote nguyên văn:**
  > *"Trước đây bot cũ quăng ra menu 5-6 dòng bắt chọn số 1, 2, 3 nhìn phát ngợp. Bot mới hỏi thẳng 2 lựa chọn sát với tuần này nên mình chọn được ngay mà không bị loãng kênh."*
- **Điểm kẹt:** Người dùng buột miệng hỏi có thể bấm nút (button) để chọn luôn thay vì phải gõ lại chữ "Lab 02" không.
- **Quyết định thay đổi:** 
  - Đưa tính năng Discord Interactive Buttons vào backlog kỹ thuật tuần tới.
  - Hiện tại, kịch bản Low-confidence với 2 lựa chọn cụ thể đã giải quyết triệt để 54.5% phàn nàn về bot cũ gây loãng kênh chat.

---

### Người 3: Trần Mạnh Hùng — Học viên K4 lớp 3B (Willing User 3)
- **Task giao:** "Bạn hãy thử hỏi bot 2 câu: (1) một thông tin chưa từng được thông báo như 'Bao giờ có điểm thi cuối kỳ?' và (2) nhờ bot 'Viết code Python giải bài tập'."
- **Thời gian hoàn thành:** 1 phút 38 giây
- **Hành vi quan sát:**
  - **Case 1 (No-grounding - Lớp ①):** Gõ hỏi điểm thi cuối kỳ. Bot phản hồi: *"Mình chưa tìm thấy thông tin này trong tài liệu thông báo chính thức. Bạn tag @TA ở kênh #ho-tro để được giải đáp nhé!"*. Người dùng gật đầu đồng tình, xác nhận bot không hề bịa ngày thi.
  - **Case 2 (Out-of-scope - Lớp ③):** Gõ nhờ viết code Python. Bot từ chối lịch sự: *"Mình chỉ hỗ trợ tra cứu thông tin và quy chế vận hành khóa học, không hỗ trợ viết code giải bài tập. Bạn trao đổi thêm tại #thao-luan nhé!"*.
- **Quote nguyên văn:**
  > *"Rất thích điểm bot không biết thì nói thẳng là không biết rồi hướng dẫn tag TA, chứ không bịa linh tinh làm học viên tưởng thật rồi lỡ việc."*
- **Điểm kẹt:** Người dùng hỏi liệu bot có thể tự động ping thẳng TA vào thread này luôn được không thay vì chỉ hướng dẫn học viên tag.
- **Quyết định thay đổi:** Giữ nguyên cơ chế Conditional Handoff hiện tại (hướng dẫn tag vào `#ho-tro` để tránh tình trạng spam notification làm phiền TA); ghi nhận tính năng tự động chuyển dispatch ticket vào backlog nâng cao.

---

## 2. Bốn dòng tổng kết theo chuẩn §4.2 `02-guide.md`

1. **Chủ đề lặp nhiều nhất:** 
   100% người dùng (3/3) đều đánh giá cao tính **minh bạch và xác thực** — câu trả lời có nguồn trích dẫn cụ thể (`📌 Nguồn: #[kênh]`) và bot **tuyệt đối không ảo giác (Zero Hallucination)** khi gặp câu hỏi chưa có tài liệu.
2. **1–2 thay đổi làm trước demo:**
   - Chuẩn hóa format hiển thị nguồn trích dẫn với emoji `📌 Nguồn:` nổi bật và ghi rõ ngày thông báo để học viên dễ quét mắt.
   - Nhắc rõ kênh `#ho-tro` trong mẫu fallback No-Grounding để học viên biết chính xác nơi cần tìm TA.
3. **Giữ nguyên có lý do:**
   - Giữ nguyên việc **từ chối giải bài tập / viết code** (Out-of-scope) và **từ chối quyết định thay đổi hạn nộp** (Non-goals), vì bot được định vị là trợ lý vận hành lớp học, không làm thay việc học thuật.
   - Giữ nguyên cơ chế **hỏi làm rõ (Low-confidence)** khi input mơ hồ thay vì cố đoán — đúng nguyên tắc HAX G10 và chi phí sai sót (cost-of-error) cao của domain giáo dục.
4. **Đưa vào backlog (nếu có thêm 1 tuần):**
   - Tích hợp Discord Interactive Components (nút bấm chọn nhanh Lab/Project thay vì nhập text).
   - Tự động hóa luồng mở Ticket hỗ trợ cho TA khi kích hoạt nhánh No-Grounding.

---

## 3. Trích xuất ≥2 Quote nguyên văn gửi Thắng làm Slide 5

Hai quote đắt giá nhất phản ánh đúng sự chuyển biến từ "nỗi đau cũ" sang "giải pháp mới":

1. **Bùi Việt Anh (Học viên K4 lớp 3B):**
   > *"Bot trả lời thẳng vào ngày giờ nộp kèm link kênh thông báo nên rất an tâm, không sợ bị troll hay nhầm hạn cũ như trước."*  
   *(Minh chứng cho: Tính năng trích dẫn nguồn xác thực giải quyết triệt để nỗi đau 78.6% tìm deadline và 71.4% cần nguồn).*

2. **Trần Mạnh Hùng (Học viên K4 lớp 3B):**
   > *"Rất thích điểm bot không biết thì nói thẳng là không biết rồi hướng dẫn tag TA, chứ không bịa linh tinh làm học viên tưởng thật rồi lỡ việc."*  
   *(Minh chứng cho: Quy tắc Zero-Hallucination & HAX G10 bảo vệ học viên khỏi cost-of-error khi lỡ deadline).*
