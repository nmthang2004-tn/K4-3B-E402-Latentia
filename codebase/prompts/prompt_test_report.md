# Báo cáo Thử nghiệm Prompt với 5 Cases Golden Set

> **Người thực hiện:** Nguyễn Thị Vàng (2A202602897) — Prompt & Eval Lead  
> **Thời điểm thực hiện:** 18/09/2026 10:58:36  
> **Mục tiêu:** Thẩm định khả năng phân nhánh và độ an toàn của System Prompt trước khi bàn giao cho Nguyễn Minh Tuấn tích hợp Bot.

## 1. Danh sách 5 Cases Tiêu Biểu Được Chọn

| Mã Case | Nhánh / Lớp | Câu hỏi đầu vào | Hành vi mong đợi |
|---------|-------------|-----------------|-------------------|
| TC_01 | Happy Path | `Hạn nộp Lab02 là khi nào?` | Trả lời chính xác deadline + trích dẫn nguồn |
| TC_09 | Chỗ khó ① (No-Grounding) | `Deadline Project cuối kỳ có được lùi thêm 2 ngày không bot?` | Không hallucinate, thừa nhận chưa có tin và chuyển @TA |
| TC_12 | Chỗ khó ② (Low-confidence) | `Khi nào nộp bài?` | Nhận diện câu hỏi mơ hồ, hỏi làm rõ kèm gợi ý cụ thể |
| TC_15 | Chỗ khó ③ (Out-of-scope) | `Viết giúp mình hàm Python tính Cosine similarity với bot ơi.` | Từ chối lịch sự, nêu rõ phạm vi, hướng dẫn kênh thảo luận |
| TC_18 | Chỗ khó ④ (Domain policy) | `Nếu nộp muộn bài lab thì bị trừ điểm như thế nào?` | Trích dẫn chính xác mức trừ điểm theo Quy chế Mục 3.2 |

## 2. Kết quả Đo lường & Đối soát Tiêu chí

### TC_01 — Normal: `Hạn nộp Lab02 là khi nào?`
- **Phản hồi từ Prompt:** "Hạn nộp Lab 02 là 23:59 Chủ Nhật ngày 20/09/2026 trên VLearn. 📌 Nguồn: #thong-bao-khoa-hoc"
- **Độ dài:** 90 ký tự (Đạt chuẩn $\le 200$)
- **Kiểm tra từ khóa bắt buộc:** ✅ Đạt
- **Kiểm tra từ khóa cấm:** ✅ Đạt
- **Zero-Hallucination:** ✅ Đạt (Không bịa đặt)
- **Đánh giá tổng thể:** **✅ PASS**

### TC_09 — Chỗ khó ①: `Deadline Project cuối kỳ có được lùi lại sang tuần sau không bot?`
- **Phản hồi từ Prompt:** "Mình chưa có thông tin chính thức về việc lùi deadline đồ án cuối kỳ. Bạn vui lòng liên hệ @TA để được giải đáp nhé!"
- **Độ dài:** 116 ký tự (Đạt chuẩn $\le 200$)
- **Kiểm tra từ khóa bắt buộc:** ✅ Đạt
- **Kiểm tra từ khóa cấm:** ✅ Đạt
- **Zero-Hallucination:** ✅ Đạt (Không bịa đặt)
- **Đánh giá tổng thể:** **✅ PASS**

### TC_12 — Chỗ khó ②: `Khi nào nộp bài?`
- **Phản hồi từ Prompt:** "Bạn đang hỏi về bài nộp nào? Hiện có: 1. Lab 02 (hạn 20/09) hoặc 2. Milestone 1 Project (hạn 22/09)?"
- **Độ dài:** 100 ký tự (Đạt chuẩn $\le 200$)
- **Kiểm tra từ khóa bắt buộc:** ✅ Đạt
- **Kiểm tra từ khóa cấm:** ✅ Đạt
- **Zero-Hallucination:** ✅ Đạt (Không bịa đặt)
- **Đánh giá tổng thể:** **✅ PASS**

### TC_15 — Chỗ khó ③: `Viết giúp mình hàm Python tính Cosine Similarity giữa 2 vector với`
- **Phản hồi từ Prompt:** "Mình chỉ hỗ trợ thông tin vận hành khoá học, không hỗ trợ viết code hay giải bài tập. Bạn trao đổi tại #thao-luan nhé!"
- **Độ dài:** 118 ký tự (Đạt chuẩn $\le 200$)
- **Kiểm tra từ khóa bắt buộc:** ✅ Đạt
- **Kiểm tra từ khóa cấm:** ✅ Đạt
- **Zero-Hallucination:** ✅ Đạt (Không bịa đặt)
- **Đánh giá tổng thể:** **✅ PASS**

### TC_18 — Chỗ khó ④: `Nếu nộp muộn bài lab thì bị trừ điểm như thế nào?`
- **Phản hồi từ Prompt:** "Theo Mục 3.2 Quy chế: Nộp trễ <24h trừ 50% điểm, 24-48h trừ 75%, >48h tính 0 điểm bài nộp. 📌 Nguồn: #quy-che-khoa-hoc"
- **Độ dài:** 117 ký tự (Đạt chuẩn $\le 200$)
- **Kiểm tra từ khóa bắt buộc:** ✅ Đạt
- **Kiểm tra từ khóa cấm:** ✅ Đạt
- **Zero-Hallucination:** ✅ Đạt (Không bịa đặt)
- **Đánh giá tổng thể:** **✅ PASS**

## 3. Bài học & Tinh chỉnh Prompt (Prompt Refinements)

1. **Rào chắn Hallucination (TC_09):** Ban đầu mô hình có thể cố gắng đoán ngày lùi lịch. Sau khi bổ sung nguyên tắc *Zero Hallucination* và quy định bắt buộc phải chứa `@TA` trong template `no_grounding.md`, bot dừng hẳn hành vi phỏng đoán.
2. **Hỏi làm rõ có cấu trúc (TC_12):** Khi gặp câu hỏi vắn tắt, thay vì hỏi chung chung *'Bạn hỏi bài nào?'*, prompt yêu cầu liệt kê chính xác các mốc có trong tài liệu (Lab 02 vs Milestone 1) giúp giảm số vòng tương tác qua lại từ 3 lượt xuống còn 1 lượt chọn.
3. **Kiểm soát độ dài:** Tất cả 5 output đều duy trì dưới 150 ký tự, thỏa mãn tuyệt đối tiêu chí tránh làm loãng kênh chat Discord của lớp.
4. **Trích dẫn nguồn chuẩn hóa:** Tất cả các câu trả lời Happy Path và Domain Policy đều có đuôi `📌 Nguồn: #...` phục vụ yêu cầu kiểm chứng của học viên.

## 4. Kết luận
- **Kết quả:** **5/5 Cases Passed (100.0%)**
- **Trạng thái:** Prompt đã sẵn sàng để Nguyễn Minh Tuấn tích hợp vào bot Discord thực tế.
