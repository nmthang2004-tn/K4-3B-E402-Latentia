# Reflection Cá Nhân — Checkpoint 5 & Hackathon AI20k

- **Họ và tên:** Nguyễn Minh Tuấn
- **Mã học viên:** 2A202602420
- **Nhóm:** Latentia (K4-3B-E402)
- **Vai trò:** Build Prototype, Discord Bot AI Client, Logging & Video Demo

---

## 1. Phần việc tôi đã phụ trách và hoàn thành
- **CP2 (Prototype & Flow):** Xây dựng Clickable Prototype tương tác (`codebase/prototype/index.html`) mô phỏng giao diện Discord dark mode, tích hợp đầy đủ 4 nhánh điều hướng cốt lõi (Happy path, Low-confidence, No-grounding, Correction) và các nguyên tắc HAX/PAIR (G1, G8, G9, G10, G11).
- **CP3 (AI Integration & Logging):**
  - Tích hợp gọi mô hình AI thật (`codebase/ai_client.py`) qua Gemini API với cơ chế fallback model.
  - Xây dựng hệ thống lưu vết (`codebase/logger.py` và `codebase/logs/ai_interactions.jsonl`) ghi nhận toàn bộ prompt, context, câu trả lời, latency và confidence score.
  - Phối hợp chạy bộ kiểm thử Golden Set và ghi nhận kết quả thực tế.
- **CP5 (Backup Demo & Pitch Prep):** 
  - Soạn kịch bản và quay video demo dự phòng (`demo_backup.mp4`) bao gồm 1 case chuẩn có trích dẫn và 1 case khó fallback an toàn.
  - Đảm bảo hệ thống prototype/bot sẵn sàng cho phần Live Demo và xử lý câu hỏi thử thách từ Ban giám khảo ở CP6.

---

## 2. Bài học kỹ thuật lớn nhất (What I learned)
- **Chi phí của sai lầm (Cost-of-error):** Khi làm trợ lý thông tin khóa học, việc bot trả lời sai deadline hoặc bịa đặt lịch thi gây hậu quả rất nghiêm trọng cho học viên. Do đó, việc xây dựng cơ chế kiểm soát nghiêm ngặt (Strict Grounding) và phân nhánh tự động (Conditional Automation) để bot tự nhận biết khi thiếu căn cứ và fallback về TA quan trọng hơn nhiều so với việc cố trả lời bằng mọi giá.
- **Vibe-coding có trách nhiệm:** Việc dùng AI hỗ trợ sinh code giúp tăng tốc độ làm prototype rất nhanh, nhưng bản thân lập trình viên phải hiểu rõ từng luồng logic, cách thức gọi API, cơ chế bắt ngoại lệ (rate limit, network timeout) và cơ chế logging thì mới có thể tự tin làm chủ sản phẩm khi đem ra thuyết trình và demo thực tế.

---

## 3. Nếu có thêm 1 tuần, tôi sẽ cải thiện điều gì?
1. **Tích hợp Discord Webhook / Bot Gateway chính thức:** Triển khai bot trực tiếp lên server Discord của khóa học kèm cơ chế phân quyền kênh, tự động lắng nghe thread thông báo từ BTC.
2. **Cơ chế Hybrid Retrieval & Semantic Cache:** Tích hợp vector search (RAG) kết hợp keyword search để truy xuất văn bản chính xác hơn và cache các câu hỏi trùng lặp để giảm latency cũng như tiết kiệm chi phí API.
3. **Admin Dashboard:** Xây dựng giao diện web cho TA xem danh sách các câu hỏi fallback mà bot chưa trả lời được để cập nhật dữ liệu tài liệu tức thì.
