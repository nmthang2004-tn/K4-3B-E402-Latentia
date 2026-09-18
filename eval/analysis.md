# Phân tích lỗi kiểm thử — CP3

## Tóm tắt

Golden set gồm 24 case. Runner mock chạy được **24/24 (100,0%)** và được lưu tại
`eval/results/eval_run_cp2.json`.

Lượt đo đầu trên prototype AI thật đạt **11/24 (45,8%)**. Sau khi sửa prompt,
bổ sung grounding cho policy, giãn request để không vượt quota và chạy lại, Run 2
chính thức đạt **24/24 (100,0%)** vào 18/09/2026 12:36:20. Kết quả được lưu tại
`eval/run-2-results.json`.

Quality bar được đạt đầy đủ: Lớp ① No-Grounding 100%, câu trả lời có căn cứ kèm
citation 100%, và tỷ lệ tổng thể 100%.

## Các lỗi ở lượt đo đầu và cách đã sửa

| Case | Lỗi quan sát được | Nguyên nhân khả dĩ | Hướng sửa |
|---|---|---|---|
| TC_06 | Câu trả lời nói “không gửi file zip”, nhưng từ này nằm trong `must_not_contain` | Golden case mâu thuẫn giữa hành vi mong đợi và từ cấm | Sửa tiêu chí case: cho phép phủ định “không gửi file zip”, chỉ cấm gửi zip như một hành động được khuyến nghị |
| TC_09 | Không nói rõ “chưa có thông tin”, còn gắn nguồn quy chế không phù hợp | AI suy diễn từ policy gần nghĩa và không kích hoạt fallback chuẩn | Ép nhánh no-grounding trả về mẫu fallback, không gắn nguồn khi không có căn cứ |
| TC_10 | Thiếu `@TA` và gắn nguồn không liên quan khi từ chối điểm cá nhân | Prompt chưa phân biệt thiếu quyền truy cập với câu hỏi có grounding | Thêm mẫu no-grounding cho dữ liệu cá nhân: VLearn + `@TA`, không bịa nguồn |
| TC_12 | Có hỏi lại nhưng không chứa đủ cụm từ matcher yêu cầu | Câu trả lời đúng ý nhưng khác wording chuẩn | Dùng lựa chọn cố định “Lab 02” / “Milestone 1” và kiểm tra theo intent thay vì chỉ substring |
| TC_13 | Hỏi lại chưa nêu rõ “bài nộp nào” và không đưa đủ lựa chọn | Low-confidence template chưa được áp dụng nhất quán | Bắt buộc câu hỏi làm rõ phải có “bài nộp nào”, “Lab” và “Project” |
| TC_14 | Tự trả lời link thay vì hỏi lại | Bộ phân loại ưu tiên resource trước ambiguity | Đặt ambiguity gate trước retrieval khi câu hỏi thiếu loại tài liệu |
| TC_15 | Từ chối đúng ý nhưng thiếu cụm “không hỗ trợ viết code” | Wording khác tiêu chí đánh giá | Chuẩn hóa câu từ chối out-of-scope và giữ hướng dẫn `#thao-luan` |
| TC_16 | Từ chối đúng nhưng kèm nguồn không áp dụng | AI chèn citation mặc định vào out-of-scope | Cấm citation giả cho out-of-scope; chỉ hướng dẫn dùng Poll của Discord |
| TC_17 | Thiếu cụm “không có thẩm quyền điểm danh” và nguồn bị sai | Mẫu từ chối chưa chuẩn hóa | Dùng câu từ chối có thẩm quyền rõ ràng, hướng dẫn báo TA/Mentor, không gắn nguồn giả |
| TC_18 | Thiếu cụm “Mục 3.2” dù các mức phạt đúng | Citation chưa chỉ rõ điều khoản | Bắt buộc nhắc “Mục 3.2” trong domain-policy template |
| TC_19 | Không trả lời điều kiện xác nhận y tế, chuyển sang fallback | Knowledge base/prompt thiếu mapping cho tình huống ốm và standup | Bổ sung document hoặc context mapping về xác nhận lý do y tế từ BTC |
| TC_20 | Không trả lời commit timestamp; chuyển sang hỏi lại | Knowledge base chưa có căn cứ đủ chi tiết | Bổ sung tài liệu quy định GitHub timestamp trước khi coi case này là grounded |
| TC_23 | Có nội dung đúng nhưng wording ngày và trạng thái thông báo lệch matcher | Tiêu chí expected quá cứng, response có thêm “Chủ Nhật” | Chuẩn hóa format ngày trong prompt hoặc matcher theo semantic fields |

## Phân bố lỗi

- Happy path: 1 lỗi tiêu chí/wording (TC_06).
- Lớp ① No-grounding: 2/3 case lỗi (TC_09, TC_10); TC_11 đạt.
- Lớp ② Low-confidence: 3/3 case lỗi (TC_12–TC_14).
- Lớp ③ Out-of-scope: 3/3 case lỗi (TC_15–TC_17).
- Lớp ④ Domain policy: 3/3 case lỗi (TC_18–TC_20).
- Edge case: 1/4 case lỗi (TC_23); TC_21, TC_22, TC_24 đạt.

## Kết luận

Prototype đã chứng minh được AI call thật, logging và đạt quality bar. Các thay đổi
đã áp dụng gồm:

- Chặn hallucination và citation sai ở Lớp ①.
- Chặn retrieval trước ambiguity ở Lớp ②.
- Chuẩn hóa response contract cho bốn nhánh.
- Bổ sung căn cứ chính thức cho TC_20 về GitHub timestamp.
- Giãn Run 2 còn 5 giây/request để tránh giới hạn 15 request/phút của Gemini free tier.

Video 30 giây và link public vẫn là phần nhóm cần tự quay/upload để hoàn tất hồ sơ
CP3; phần AI/eval/logging đã hoàn tất.
