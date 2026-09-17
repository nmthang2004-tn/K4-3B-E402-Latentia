# Golden Set & Khung Kiểm Thử (Eval Framework) — Trợ lý Discord

> **Chủ trì xây dựng:** Nguyễn Thị Vàng (2A202602897) — Prompt/UX & Eval Lead  
> **Áp dụng:** Nhóm Latentia (K4-3B-E402) · Zone C1 · Track B1  
> **Quy chuẩn đối chiếu:** `02-guide.md` §2.5 & §2.6, Rubric R4 (15 điểm)

---

## 1. User Input Grid (Ma Trận Phủ Ca Kiểm Thử)

Để tránh việc sinh test case theo cảm tính hoặc thiên lệch toàn Happy Path, bộ Golden Set được thiết kế dựa trên **User Input Grid 4 chiều**:

| Loại thông tin (Topic) | Độ rõ của Input | Rủi ro sai sót (Cost of Error) | Hành vi mong đợi (Branch) | Số case | Mã case đại diện |
|------------------------|-----------------|--------------------------------|---------------------------|---------|-------------------|
| **Deadline / Lịch nộp** | Rõ ràng | **Cao** (sai thì mất điểm) | Happy Path (Trả lời + Cite nguồn) | 4 | `TC_01`, `TC_04`, `TC_06`, `TC_07` |
| **Lịch trình / Standup** | Rõ ràng | Trung bình (trễ giờ họp) | Happy Path (Trả lời + Cite nguồn) | 3 | `TC_03`, `TC_08`, `TC_19` |
| **Link tài liệu / Hướng dẫn** | Rõ ràng | Thấp (tốn công tìm) | Happy Path (Trả lời link trực tiếp) | 2 | `TC_02`, `TC_05` |
| **Thông tin chưa công bố** | Rõ ràng | **Rất cao** (lan truyền tin sai) | Lớp ① No-Grounding (Chuyển TA) | 3 | `TC_09`, `TC_10`, `TC_11` |
| **Câu hỏi vắn tắt / mơ hồ** | Mơ hồ, thiếu ngữ cảnh | Trung bình (trả lời nhầm bài) | Lớp ② Low-Confidence (Hỏi lại G10) | 3 | `TC_12`, `TC_13`, `TC_14` |
| **Hỏi code / Làm bài hộ** | Rõ ràng | Cao (sai mục đích sản phẩm) | Lớp ③ Out-of-Scope (Từ chối G1) | 3 | `TC_15`, `TC_16`, `TC_17` |
| **Quy chế phạt / Điểm danh** | Rõ ràng | **Rất cao** (học viên vi phạm) | Lớp ④ Domain Policy (Trích điều khoản) | 3 | `TC_18`, `TC_19`, `TC_20` |
| **Viết tắt / Teencode / Bẫy** | Biến thể câu chữ | Trung bình - Cao | Edge Cases (Hiểu đúng ý / Bác tin đồn) | 3 | `TC_21`, `TC_22`, `TC_23`, `TC_24` |

**Tổng số test cases:** 24 cases (vượt yêu cầu tối thiểu ≥ 20 cases).  
Trong đó: **14/24 cases (58.3%)** được trích xuất hoặc phát triển trực tiếp từ khảo sát thực tế của 14 học viên lớp 3B.

---

## 2. Ba Chiều Chất Lượng Kiểm Chứng Được (Quality Dimensions)

Theo khung PAIR 2.3 *"Evolve AI with evaluation"*:

1. **Factuality (Đúng sự thật & Có căn cứ):**
   - *Định nghĩa kiểm chứng:* 100% chi tiết trong câu trả lời phải đối chiếu được với Knowledge Base (thông báo chính thức). Tuyệt đối không hallucinate. Nếu không có dữ liệu, bắt buộc phải trả về trạng thái "Chưa có thông tin" và tag TA.
   - *Thang đo:* **Pass / Fail** (Điều kiện cứng: Fail ngay nếu bịa thông tin).

2. **Relevance & Precision (Đúng trọng tâm & Đúng mục đích):**
   - *Định nghĩa kiểm chứng:* Câu trả lời tập trung đúng vào câu hỏi, không xuất hiện các đoạn văn quảng bá, không trả về menu hỏi lại dài dòng làm loãng kênh Discord.
   - *Thang đo:* Thang điểm 1 - 5 (Đạt khi ≥ 4/5).

3. **Conciseness & Source Citation (Độ ngắn gọn & Kèm trích dẫn):**
   - *Định nghĩa kiểm chứng:* Độ dài văn bản ≤ 200 ký tự (hoặc ≤ 3 gạch đầu dòng), luôn có dòng `📌 Nguồn: [Kênh/Tài liệu]` đối với các câu trả lời Happy Path và Domain Policy. Có action buttons dự phòng.
   - *Thang đo:* **Pass / Fail**.

---

## 3. Quality Bar (Chuẩn Chất Lượng Khóa Cứng)

> 🔒 **Cam kết Quality Bar (khóa tại CP4):**  
> 1. **Tỷ lệ vượt qua tổng thể:** `Pass Rate ≥ 85%` (ít nhất 21/24 cases đạt chuẩn).  
> 2. **Điều kiện cứng (Zero-Hallucination):** 100% case thuộc **Lớp ① (No-Grounding)** không được phép bịa đặt hay đoán mò hạn nộp; 100% phải kích hoạt fallback chuyển TA.  
> 3. **Điều kiện nguồn:** 100% câu trả lời thành công ở Happy Path bắt buộc phải có trích dẫn nguồn.

---

## 4. Danh Sách Chi Tiết 24 Golden Test Cases

| ID | Nhánh | Phân lớp | Input của học viên | Hành vi mong đợi & Kết quả chuẩn | Nguồn dữ liệu |
|---|---|---|---|---|---|
| `TC_01` | Happy Path | Thường | *"Hạn nộp Lab02 là khi nào?"* | Trả lời: 23:59 ngày 20/09/2026. Nguồn: #thong-bao-khoa-hoc | Chatlog/Khảo sát |
| `TC_02` | Happy Path | Thường | *"Cho mình xin link slide và tài liệu học tập với"* | Trả lời link kho tài nguyên VLearn chính thức | Khảo sát (50%) |
| `TC_03` | Happy Path | Thường | *"Lịch standup sáng lớp 3B mấy giờ bắt đầu?"* | Trả lời: 08:30 sáng tại phòng E402 / Voice Discord | Khảo sát (42.9%) |
| `TC_04` | Happy Path | Thường | *"Milestone 1 Project nộp trước mấy giờ ngày nào?"* | Trả lời: 21:00 ngày 22/09/2026 kèm nguồn thông báo | Chatlog K4 |
| `TC_05` | Happy Path | Thường | *"Gặp lỗi kỹ thuật thì tạo ticket ở kênh nào?"* | Hướng dẫn gõ lệnh /ticket tại #ho-tro-ky-thuat | Khảo sát (28.6%) |
| `TC_06` | Happy Path | Thường | *"Nộp bài Lab 02 qua hình thức nào, có cần gửi zip không?"* | Nêu rõ nộp link GitHub trên VLearn, không nộp zip | Tài liệu hướng dẫn |
| `TC_07` | Happy Path | Thường | *"Milestone 1 cả nhóm cùng nộp hay chỉ nhóm trưởng nộp?"* | Nêu rõ mỗi nhóm nộp 1 bản duy nhất do nhóm trưởng nộp | Quy định nộp bài |
| `TC_08` | Happy Path | Thường | *"Standup lớp 3B kéo dài trong bao lâu?"* | Trả lời: Tối đa 15 phút | Quy định lớp học |
| `TC_09` | No-Grounding | **Chỗ khó ①** | *"Deadline Project cuối kỳ có được lùi sang tuần sau không?"* | Không bịa đặt. Báo chưa có thông tin chính thức, tag @TA | Khảo sát thực tế |
| `TC_10` | No-Grounding | **Chỗ khó ①** | *"Điểm bài Lab 01 của mình được mấy điểm thế bot?"* | Từ chối do không có dữ liệu điểm cá nhân, hướng dẫn lên VLearn | Chatlog thực tế |
| `TC_11` | No-Grounding | **Chỗ khó ①** | *"Lịch thi giữa kỳ môn này diễn ra vào ngày nào?"* | Nêu rõ không có thi giữa kỳ (đánh giá qua Lab/Project), hỏi TA | Kịch bản rủi ro |
| `TC_12` | Low-Confidence | **Chỗ khó ②** | *"Khi nào nộp bài?"* | Không đoán bừa. Hỏi lại: bạn muốn hỏi Lab 02 hay Milestone 1? | Khảo sát (54.5% kêu bot k hiểu) |
| `TC_13` | Low-Confidence | **Chỗ khó ②** | *"Mấy giờ hết hạn?"* | Yêu cầu người dùng nêu rõ tên bài tập/mục nộp bài | Chatlog K4 |
| `TC_14` | Low-Confidence | **Chỗ khó ②** | *"Link bài học ở đâu?"* | Hỏi lại xem học viên cần slide lý thuyết hay link bài tập | Chatlog K4 |
| `TC_15` | Out-of-Scope | **Chỗ khó ③** | *"Viết giúp mình hàm Python tính Cosine Similarity với"* | Từ chối lịch sự: Bot chỉ hỗ trợ vận hành, mời sang #thao-luan | Chatlog thực tế |
| `TC_16` | Out-of-Scope | **Chỗ khó ③** | *"Tạo một vote bình chọn giờ họp nhóm cho team mình với"* | Từ chối tạo poll thay, hướng dẫn dùng tính năng Poll của Discord | Kịch bản rủi ro |
| `TC_17` | Out-of-Scope | **Chỗ khó ③** | *"Điểm danh hộ mình sáng nay với, mình vào trễ 10p"* | Từ chối vì không có thẩm quyền điểm danh thay, nhắc báo TA | Quy chế |
| `TC_18` | Domain Policy | **Chỗ khó ④** | *"Nếu nộp muộn bài lab thì bị trừ điểm như thế nào?"* | Trích dẫn Mục 3.2: <24h trừ 50%, 24-48h trừ 75%, >48h 0đ | Khảo sát (35.7%) |
| `TC_19` | Domain Policy | **Chỗ khó ④** | *"Bị ốm không tham gia standup thì có bị phạt trừ điểm không?"* | Nêu rõ cần xác nhận lý do y tế từ BTC để được miễn trừ | Quy chế lớp học |
| `TC_20` | Domain Policy | **Chỗ khó ④** | *"Commit sau deadline nhưng push trước giờ thì tính sao?"* | Giải thích tính theo commit timestamp trên GitHub | Quy chế kỹ thuật |
| `TC_21` | Edge Case | Hiếm | *"dl lab2 la khi nao the bot oi"* | Hiểu teencode "dl lab2", trả lời 23:59 ngày 20/09 | Ngôn ngữ học viên |
| `TC_22` | Edge Case | Hiếm | *"han nop ms1 pj la hom nao"* | Hiểu viết tắt "ms1 pj", trả lời 21:00 ngày 22/09 | Ngôn ngữ học viên |
| `TC_23` | Edge Case | Hiếm | *"Nghe đồn Lab02 được dời hạn đến thứ Tư đúng không?"* | Bác bỏ tin đồn, khẳng định hạn vẫn là 20/09 theo thông báo | Bẫy giả định |
| `TC_24` | Edge Case | Hiếm | *"Cho hỏi hạn nộp Lab 02 và link xem slide buổi đó ở đâu?"* | Trả lời đủ cả 2 ý: hạn nộp 20/09 và link kho slide VLearn | Câu hỏi ghép |

---

## 5. Hướng Dẫn Chạy Kiểm Thử (Cho CP3 & Đánh Giá)

Hệ thống cung cấp runner tự động tại [run_eval.py](file:///d:/Download/VINUNI%20AI/DAY5/K4-3B-E402-Latentia/eval/run_eval.py):
```bash
python eval/run_eval.py
```
Runner sẽ tự động chạy qua 24 test cases, kiểm tra các từ khóa bắt buộc (`expected_output_contains`), từ khóa cấm (`must_not_contain`), cơ chế phân nhánh (`expected_branch`) và xuất báo cáo tỷ lệ Pass/Fail chi tiết phục vụ mốc CP3.
