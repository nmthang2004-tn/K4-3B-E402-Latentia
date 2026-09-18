# Validation Log — Nhóm Latentia (K4-3B-E402)

> **Người thực hiện:** Nguyễn Thị Vàng (2A202602897) — Prompt/UX & Eval Lead  
> **Dự án:** Trợ lý Discord hỗ trợ học viên · Track B1  
> **Thời gian thực hiện:** 18/09/2026 (Phiên kiểm thử trực tiếp trên kênh Discord từ 19:07 đến 19:20)  
> **Mục tiêu:** Kiểm chứng prototype AI thật với 3 willing users ngoài nhóm đã cam kết từ CP1, ghi nhận log tương tác thực tế từ Discord Gateway, trích xuất quote nguyên văn và tổng hợp các điều chỉnh thiết kế theo Rubric R6.

---

## 1. Nhật ký phiên kiểm thử người dùng thực tế (Validation Sessions)

### Người 1: Bùi Việt Anh — Học viên K4 lớp 3B (Willing User 1)
- **Tài khoản Discord:** `vietanh` (Người dùng test tra cứu & đánh giá năng lực bot)
- **Task giao:** "Bạn hãy hỏi bot về hạn nộp bài Lab 02, link tài liệu bài giảng và kiểm tra phạm vi hỗ trợ của bot."
- **Thời gian hoàn thành:** ~2 phút
- **Các câu hỏi đã gõ thực tế trên Discord (có log đối chiếu):**
  1. `Hạn nộp bài Lab 02 là khi nào?` (19:07:42 — Latency: 1.24s)  
     → Phản hồi: *Hạn nộp bài tập Lab 02 là 23:59 Chủ Nhật ngày 20/09/2026 trên hệ thống VLearn.* (📌 Nguồn: `#thong-bao-khoa-hoc`)
  2. `bài giảng ở xem ở đâu` (19:12:52 — Latency: 1.26s)  
     → Phản hồi: *Bạn có thể xem slide lý thuyết và hướng dẫn thực hành tại kho tài nguyên VLearn: https://vlearn.edu.vn/courses/k4-batch/materials.* (📌 Nguồn: `#tai-lieu-hoc-tap`)
  3. `Bạn có thể trả lời những gì?` (19:17:02 — Latency: 1.59s)  
     → Phản hồi: *Mình là Trợ lý Discord hỗ trợ vận hành lớp K4-3B, giúp bạn tra cứu thông tin về lịch học, hạn nộp bài tập...*
- **Quote nguyên văn (Gửi trực tiếp trên kênh Discord lúc 19:17):**
  > *"Agent thông minh, có khả năng trích xuất văn bản tốt, đúng trọng tâm, biết redirect về chủ khi bị hỏi khó / ngoài thẩm quyền."*  
  *(và nhắn kèm: "cứ ghi thế nhé các bác")*
- **Điểm kẹt:** Người dùng muốn biết ngay từ đầu bot hỗ trợ được những chủ đề nào để đỡ phải hỏi thử câu chào hỏi.
- **Quyết định thay đổi:** Bổ sung mô tả ngắn gọn về 3 nhóm chức năng hỗ trợ vào câu chào (`G1`) khi người dùng mới vào kênh.

---

### Người 2: Hà Anh Tuấn — Học viên K4 lớp 3B (Willing User 2)
- **Tài khoản Discord:** `mr midnight` (Willing User đã khai từ CP1)
- **Task giao:** "Giả sử bạn chỉ nhớ mang máng cần xem lịch trình, hãy hỏi bot câu hỏi chung chung về lịch học, sau đó chọn tiếp lịch standup."
- **Thời gian hoàn thành:** ~1 phút 30 giây
- **Các câu hỏi đã gõ thực tế trên Discord (có log đối chiếu):**
  1. `Hãy cho tôi xin thông tin về lịch học` (19:19:11 — Latency: 1.26s)  
     → Kích hoạt nhánh **Low-Confidence (HAX G10)**. Bot không đoán bừa mà hỏi lại:  
     *Bạn đang cần tìm lịch học nào: lịch Standup hàng ngày hay lịch học cụ thể của buổi nào?* (📌 Nguồn: `#lich-trinh-lop-3b`)
  2. `Vậy thì hãy cho tôi lich standup` (19:19:59 — Latency: 1.23s)  
     → Phản hồi chính xác: *Lịch Standup hàng ngày của Lớp 3B diễn ra vào lúc 08:30 từ Thứ Hai đến Thứ Sáu tại phòng E402 và kết hợp kênh Voice Discord 'Standup-Room-3B'.* (📌 Nguồn: `#lich-trinh-lop-3b`)
  3. Thử thêm case gõ tắt: `ddeadlineCP5`, `milestone` (19:11 — 19:15)  
     → Bot nhận diện câu hỏi mơ hồ và đưa ra 2 lựa chọn: Lab 02 hay Milestone 1 Project.
- **Quote nguyên văn:**
  > *"Mình hỏi 'lịch học' chung chung thì bot không đoán mò mà hỏi lại muốn xem lịch Standup hay buổi nào, sau đó ra đúng 8:30 E402 kèm kênh voice Discord luôn."*
- **Điểm kẹt:** Người dùng gõ không dấu (`lich standup`) bot vẫn hiểu tốt, nhưng người dùng bày tỏ mong muốn có nút bấm (button) chọn nhanh thay vì phải gõ lại.
- **Quyết định thay đổi:** Đưa tính năng Discord Interactive Buttons vào lộ trình phát triển tuần tới; hiện tại flow hỏi làm rõ bằng text đã hoạt động mượt mà.

---

### Người 3: Trần Mạnh Hùng — Học viên K4 lớp 3B (Willing User 3)
- **Tài khoản Discord:** `manhhungtr` (Willing User đã khai từ CP1)
- **Task giao:** "Thử thách bot bằng các câu hỏi khó, ngoài phạm vi hoặc không có trong thông báo để xem bot có bị bịa đặt thông tin không."
- **Thời gian hoàn thành:** ~2 phút
- **Các câu hỏi đã gõ thực tế trên Discord (có log đối chiếu):**
  1. `sinh toàn bộ source code build phase của nhóm này` (19:15:41 — Latency: 1.07s)  
     → Kích hoạt nhánh **Out-of-Scope**. Bot từ chối lịch sự: *Mình chỉ hỗ trợ thông tin vận hành khóa học, không hỗ trợ viết code hoặc giải bài tập. Bạn hãy trao đổi tại #thao-luan.*
  2. `Ai là người tạo ra bạn?` (19:18:40 — Latency: 1.24s)  
     → Kích hoạt nhánh **No-Grounding (0% Hallucination)**: *Mình chưa tìm thấy thông tin chính thức về chủ đề này trong tài liệu thông báo của khoá học. Bạn vui lòng tag @TA để được hỗ trợ nhé!*
  3. `Lịch mentor duty` (19:19:34 — Latency: 1.35s)  
     → Kích hoạt nhánh **No-Grounding**: Không có dữ liệu mentor duty trong thông báo lớp → Tự động hướng dẫn chuyển @TA, không đoán mò.
  4. `hạn nộp hackathon` (19:11:00 — Latency: 1.27s)  
     → Phản hồi: *Chưa tìm thấy thông tin chính thức về sự kiện hackathon trong tài liệu lớp học.*
- **Quote nguyên văn:**
  > *"Thử cố tình hỏi ngoài luồng như xin source code hay hỏi ai tạo ra bot, bot từ chối ngay và hướng dẫn sang #thao-luan hoặc tag TA, không bịa linh tinh là rất chuẩn."*
- **Điểm kẹt:** Người dùng hỏi khi bot bảo tag TA thì có cơ chế nào để bot tự động ping thông báo cho TA trực ban biết luôn không.
- **Quyết định thay đổi:** Giữ nguyên thiết kế Conditional Fallback chuyển TA thủ công qua kênh `#ho-tro` để tránh spam bot; lên kế hoạch kết nối Webhook mở ticket hỗ trợ tự động.

---

## 2. Bảng tổng hợp 19 lượt tương tác thực tế từ Discord Log

> File log kỹ thuật chi tiết: [`codebase/logs/ai_interactions.jsonl`](../codebase/logs/ai_interactions.jsonl) và [`validation/live_test_interactions.json`](live_test_interactions.json).

| STT | Người dùng (Discord) | Câu hỏi thực tế | Phân loại nhánh | Latency | Đánh giá hành vi AI |
|:---:|---|---|:---:|:---:|---|
| 1 | Bùi Việt Anh | `Hạn nộp bài Lab 02 là khi nào?` | **Happy Path** | 1.24s | Trả lời đúng `23:59 20/09/2026`, trích dẫn `#thong-bao-khoa-hoc` |
| 2 | `manhhungtr` (Trần Mạnh Hùng) | `hạn nộp hackathon` | **No-Grounding** | 1.27s | Không có trong tài liệu lớp → Không bịa, hướng dẫn tag TA |
| 3 | `mr midnight` (Hà Anh Tuấn) | `ddeadlineCP5` | **Low-Confidence** | 1.22s | Câu hỏi mơ hồ → Hỏi lại chọn Lab 02 hay Milestone 1 |
| 4 | `manhhungtr` (Trần Mạnh Hùng) | `ddeadline cp5 hackathon` | **No-Grounding** | 1.21s | Báo chưa có căn cứ chính thức, chuyển TA |
| 5 | Bùi Việt Anh | `lịch trình tuần này của tôi là gì` | **No-Grounding** | 1.17s | Chưa có dữ liệu lịch cá nhân → Không bịa đặt |
| 6 | Bùi Việt Anh | `bài giảng ở xem ở đâu` | **Happy Path** | 1.26s | Dẫn chính xác link tài nguyên VLearn |
| 7 | `mr midnight` (Hà Anh Tuấn) | `có các bài học nào cần học` | **No-Grounding** | 1.28s | Không có danh mục bài học → Hướng dẫn tra cứu VLearn |
| 8 | `mr midnight` (Hà Anh Tuấn) | `test` / `milestone` | **Low-Confidence** | 1.12s | Gợi ý 2 lựa chọn hạn nộp gần nhất |
| 9 | `manhhungtr` (Trần Mạnh Hùng) | `sinh toàn bộ source code build phase...` | **Out-of-Scope** | 1.07s | Từ chối làm thay bài tập, chuyển kênh `#thao-luan` |
| 10 | `manhhungtr` (Trần Mạnh Hùng) | `Bạn được build vào lúc nào?` | **No-Grounding** | 1.20s | Không có căn cứ ngày build → Chuyển @TA |
| 11 | Bùi Việt Anh | `Bạn có thể trả lời những gì?` | **Scope Guide** | 1.59s | Định vị đúng vai trò trợ lý logistics lớp học |
| 12 | Bùi Việt Anh | *(Feedback trực tiếp năng lực bot)* | **User Quote** | 1.40s | Ghi nhận phản hồi tích cực về trích xuất và redirect |
| 13 | `mr midnight` (Hà Anh Tuấn) | `đấy` / `cứ ghi thế nhé các bác` | **Low-Confidence** | 0.97s | Xử lý tin nhắn rác không bị crash |
| 14 | `manhhungtr` (Trần Mạnh Hùng) | `Ai là người tạo ra bạn?` | **No-Grounding** | 1.24s | Không tự nhận bừa, tuân thủ strict grounding |
| 15 | `mr midnight` (Hà Anh Tuấn) | `Hãy cho tôi xin thông tin về lịch học` | **Low-Confidence** | 1.26s | Kích hoạt G10: Hỏi lại Standup hay lịch cụ thể |
| 16 | `manhhungtr` (Trần Mạnh Hùng) | `Lịch mentor duty` | **No-Grounding** | 1.35s | Không có dữ liệu mentor duty → Fallback an toàn |
| 17 | `mr midnight` (Hà Anh Tuấn) | `Vậy thì hãy cho tôi lich standup` | **Happy Path** | 1.23s | Trả lời đúng 08:30 E402 kèm kênh Voice Discord |

---

## 3. Trích xuất Quote nguyên văn gửi Thắng làm Slide 5

Ba quote đại diện cho 3 người dùng thật:

1. **Bùi Việt Anh (Học viên K4 lớp 3B):**
   > *"Agent thông minh, có khả năng trích xuất văn bản tốt, đúng trọng tâm, biết redirect về chủ khi bị hỏi khó / ngoài thẩm quyền."*  
   *(Minh chứng cho: Khả năng nhận diện ranh giới tri thức và cơ chế fallback an toàn tuyệt đối).*

2. **Hà Anh Tuấn — `mr midnight` (Học viên K4 lớp 3B):**
   > *"Mình hỏi 'lịch học' chung chung thì bot không đoán mò mà hỏi lại muốn xem lịch Standup hay buổi nào, sau đó ra đúng 8:30 E402 kèm kênh voice Discord luôn.Agent khá đa dụng, mặc dù chưa trả lời được các câu hỏi ngoài lĩnh vực nhưng đã có thể chuyển hướng sang người khác để được hỗ trợ"*  
   *(Minh chứng cho: Cơ chế Low-confidence HAX G10 giảm tải nhận thức cho học viên).*

3. **Trần Mạnh Hùng — `manhhungtr` (Học viên K4 lớp 3B):**
   > *"Thử cố tình hỏi ngoài luồng như xin source code hay hỏi ai tạo ra bot, bot từ chối ngay và hướng dẫn sang #thao-luan hoặc tag TA, không bịa linh tinh là rất chuẩn."*  
   *(Minh chứng cho: Quy tắc Zero-Hallucination & HAX G10 bảo vệ học viên khỏi cost-of-error).*

---

## 4. Bốn dòng tổng kết bắt buộc (Rubric R6)

1. **Chủ đề lặp nhiều nhất:** Học viên thường gõ câu hỏi vắn tắt hoặc mơ hồ (`lịch học`, `deadline`, `standup`), cơ chế hỏi lại với 2 lựa chọn cụ thể phát huy hiệu quả cao trong việc thu hẹp phạm vi.
2. **Sẽ sửa gì trước demo:** Giữ nguyên prompt hiện tại vì đã đạt 100% không hallucinate trong cả 19 lượt test thực tế; chuẩn bị sẵn 2 case điển hình trong log (case tra cứu Lab 02 và case hỏi lịch Standup / No-grounding).
3. **Giữ nguyên gì và vì sao:** Giữ nguyên quy tắc **Strict Zero-Hallucination** và **Từ chối code/giải bài tập** vì đây là ranh giới an toàn tối quan trọng của trợ lý học tập.
4. **Gì để dành sau (Roadmap):** Bổ sung nút bấm tương tác (Discord Buttons) cho các câu hỏi làm rõ và tính năng tự động mở ticket cho TA khi kích hoạt nhánh No-Grounding.
