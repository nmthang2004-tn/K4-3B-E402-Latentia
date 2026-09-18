# BẢN REFLECTION CÁ NHÂN — CHECKPOINT 5 & HACKATHON AI20K

> **Họ và Tên:** Nguyễn Minh Thắng  
> **Mã học viên:** 2A202602706  
> **Vai trò trong nhóm:** Đội trưởng (Product Lead), Kiến trúc AI Spec, Điều phối Golden Set & Báo cáo Demo  
> **Dự án:** Trợ lý Discord hỗ trợ học viên · Track B1 — Nhóm Latentia (K4-3B-E402)  
> **Thời điểm hoàn thành:** 18/09/2026 (Checkpoint 5)

---

## 1. Tổng quan vai trò & Phạm vi đảm nhiệm xuyên suốt dự án

Trong vai trò Product Lead của nhóm Latentia, trách nhiệm chính của tôi là định vị sản phẩm, đảm bảo nhóm đi đúng lát cắt mỏng (thin slice) giải quyết nỗi đau có thật của học viên, hoàn thiện tài liệu đặc tả kỹ thuật `spec.md`, và tổng hợp hồ sơ dự án đạt chuẩn rubric chấm thi.

Các đầu việc cốt lõi tôi đã phụ trách và hoàn thành:
1. **Khởi tạo Canvas & Định hình bài toán (CP1):** Khai thác dữ liệu chatlog và phản hồi thực tế từ lớp K4, xác định JTBD cốt lõi: học viên cần tra cứu nhanh deadline/quy chế mà không bị trôi tin nhắn hay nhận câu trả lời bịa đặt.
2. **Thiết kế luồng trải nghiệm & Sơ đồ 4 đường đi (CP2):** Xây dựng sơ đồ tuần tự Mermaid trong `codebase/flow-diagram.md`, định hình 4 đường đi (Happy Path, Low-Confidence, No-Grounding, Correction) gắn chặt với các nguyên tắc HAX/PAIR (G1, G8, G9, G10, G11).
3. **Đặc tả AI Spec & Khóa Quality Bar (CP3 - CP4):** Hoàn thiện toàn diện `spec.md` từ §1 đến §9, thiết lập ma trận 10 kịch bản nghiệm thu, phân tích chi phí sai sót (cost-of-error) ở mức Conditional Automation và khóa cứng Quality Bar trước hạn chót 21:00 ngày 18/9.
4. **Soạn thảo Slide thuyết trình & Báo cáo dự án (CP5):** Xây dựng cấu trúc bộ slide 6 trang theo luật "không có bằng chứng thì không có slide" (§5.1), đối chiếu số liệu từ khảo sát n=14, kết quả Golden Set 24/24 và quote thực tế từ vòng User Validation.

---

## 2. Bài học lớn nhất (Key Learnings)

- **Nguyên tắc "Lát cắt hẹp nhưng sâu":** Trong một cuộc thi giới hạn 39 giờ, sai lầm lớn nhất là cố làm một con bot trả lời được mọi thứ. Khi thu hẹp phạm vi vào thông tin logistics của lớp học kèm cam kết Zero-Hallucination và trích dẫn nguồn, sản phẩm trở nên đáng tin cậy và có giá trị thực tế ngay lập tức.
- **Spec-driven & Vibe-coding có kỷ luật:** Sử dụng AI để tăng tốc độ viết code và tạo prototype là lợi thế rất lớn, nhưng phải được neo chặt bởi tài liệu đặc tả `spec.md` và bộ kiểm thử `eval/golden_set.json`. Nếu không khóa cứng chuẩn "đạt" từ sớm, nhóm sẽ rất dễ rơi vào bẫy tự sửa tiêu chí để làm đẹp số liệu.

---

## 3. Nếu có thêm 1 tuần, tôi sẽ ưu tiên điều gì?

1. **Mở rộng phạm vi dữ liệu tự động (Auto-sync Channel Announcement):** Xây dựng crawler tự động đọc các tin nhắn ghim từ kênh thông báo chính thức của BTC để cập nhật context theo thời gian thực mà không cần nạp thủ công.
2. **A/B Testing trong môi trường lớp học thật:** Đưa bot vào thử nghiệm trực tiếp tại kênh chat chính của lớp 3B, đo lường tỷ lệ câu hỏi học viên tra cứu thành công so với số lượng câu hỏi TA phải trả lời thủ công.
3. **Hoàn thiện giao diện Web Dashboard:** Cung cấp giao diện quản trị cho TA xem lịch sử fallback và gắn nhãn các câu hỏi mới phát sinh.
