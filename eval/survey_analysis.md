# Báo cáo Phân tích Khảo sát Học viên (Survey Analysis Report)

> **Chủ trì thực hiện:** Nguyễn Thị Vàng (2A202602897) — Prompt/UX & Eval Lead  
> **Dự án:** Trợ lý Discord hỗ trợ học viên (Nhóm Latentia · K4-3B-E402) · Track B1  
> **Đối tượng khảo sát:** $n = 14$ học viên tuần đầu lớp K4-3B  
> **Dữ liệu thô đối chiếu:** [`Trợ lý Discord hỗ trợ học viên - Câu trả lời biểu mẫu 1.csv`](../Tr%E1%BB%A3%20l%C3%BD%20Discord%20h%E1%BB%97%20tr%E1%BB%A3%20h%E1%BB%8Dc%20vi%C3%AAn%20-%20C%C3%A2u%20tr%E1%BA%A3%20l%E1%BB%9Di%20bi%E1%BB%83u%20m%E1%BA%ABu%201.csv)

---

## 1. Mục tiêu & Phương pháp Khảo sát

Khảo sát được thiết kế và triển khai nhằm mục đích:
1. Xác thực bằng chứng thực nghiệm (Empirical Evidence) về khó khăn của học viên lớp 3B trong tuần đầu tiên.
2. Đo lường mức độ hài lòng và nhận diện các điểm lỗi cốt lõi (Failure Modes) của bot hỗ trợ hiện tại trên Discord.
3. Thu thập insight định tính và nguyện vọng người dùng để trực tiếp định hình:
   - Quy tắc **Grounding & Zero Hallucination** trong System Prompt.
   - Cơ chế phân luồng **4 đường đi trải nghiệm** (Happy Path, Low-Confidence, No-Grounding, Out-of-Scope).
   - Xây dựng **Golden Set 24 cases** phản ánh trung thực nhu cầu học viên.

---

## 2. Kết quả Phân tích Định lượng (Quantitative Insights)

### 2.1. Nhu cầu thông tin & Khó khăn thường gặp (Câu 1)
- **78.6% (11/14 học viên)** gặp khó khăn lớn nhất khi tìm thông tin về **Deadline / Lịch nộp bài**.
- **50.0% (7/14 học viên)** gặp khó khăn khi tìm kiếm link phòng và giờ họp **Daily Standup**.
- **50.0% (7/14 học viên)** vướng mắc khi tìm **Link tài liệu / Bài giảng / Hướng dẫn**.
- **35.7% (5/14 học viên)** bối rối về **Quy định khoá học** (quy chế trừ điểm nộp muộn, vắng standup).
- **35.7% (5/14 học viên)** cần hỗ trợ mở **Ticket kỹ thuật**.
- *Chỉ có 1/14 học viên (7.1%)* phản hồi "Hầu như không gặp khó khăn".

> **Kết luận thiết kế:** Trợ lý AI tập trung vào lát cắt hẹp: Tra cứu hạn nộp bài, standup, link tài liệu và quy định với trích dẫn nguồn chuẩn xác.

### 2.2. Hành vi tìm kiếm & Thời gian lãng phí (Câu 2, 3, 4)
- Khi cần tìm thông tin: 50.0% dùng Discord Search, 28.6% xem tin nhắn ghim (Pinned messages), 21.4% đã thử hỏi bot.
- **Thời gian tìm kiếm:**
  - 14.3% (2/14): Có lúc hoàn toàn không tìm được thông tin.
  - 14.3% (2/14): Mất trên 10 phút.
  - 21.4% (3/14): Mất 5–10 phút.
  - 14.3% (2/14): Mất 3–5 phút.
  - $\rightarrow$ **Tổng cộng 64.3% (9/14)** mất từ 3 phút trở lên hoặc chịu thất bại khi tra cứu.
- **Trùng lặp câu hỏi:** 57.1% (8/14) đã từng gửi câu hỏi lên kênh Discord mà sau đó phát hiện câu hỏi đã được người khác hỏi từ trước.

### 2.3. Trải nghiệm với Bot Discord hiện tại (Câu 6, 8)
- 11/14 học viên (78.6%) đã từng tương tác với bot Discord hiện hữu.
- Các vấn đề gây thất vọng lớn nhất (Failure Modes) của bot cũ:
  - **54.5% (6/11):** *Không hiểu ngữ cảnh câu hỏi* $\rightarrow$ dẫn đến trả lời lạc đề.
  - **54.5% (6/11):** *Trả lời xong học viên vẫn phải tag hỏi lại TA* $\rightarrow$ không giải quyết được việc.
  - **45.5% (5/11):** *Trả lời quá dài* $\rightarrow$ gây loãng kênh chat.
  - **45.5% (5/11):** *Không biết câu trả lời lấy từ đâu (thiếu nguồn trích dẫn)* $\rightarrow$ không dám tin tưởng.
  - **36.4% (4/11):** Đưa nhiều thông tin không liên quan.
  - **27.3% (3/11):** Thông tin không chính xác hoặc đã cũ.

---

## 3. Kết quả Phân tích Định tính (Qualitative Insights & Direct Quotes)

Trích dẫn nguyên văn phản hồi từ học viên khảo sát ngày 17/09/2026:

> 💬 *"Câu trả lời ko có ích, toàn tag mod, mod ko trả lời."*  
> — Học viên lớp 3B (Dòng 15 file CSV)

> 💬 *"Trả lời quá dài, không biết câu trả lời lấy từ đâu, trả lời nhưng tôi vẫn phải hỏi TA."*  
> — Học viên lớp 3B (Dòng 3 file CSV)

> 💬 *"Khi bot không chắc chắn, hãy nói rõ rằng bot không chắc chắn và đưa nguồn để tôi tự kiểm tra, hoặc tự động chuyển câu hỏi cho TA/Mod."*  
> — Nguyện vọng của 92.8% học viên tham gia khảo sát (Câu 9)

---

## 4. Bảng Chuyển dịch từ Khảo sát sang Thiết kế Prompt & Eval

Dưới vai trò Prompt & Eval Lead, Nguyễn Thị Vàng đã trực tiếp chuyển hóa các phát hiện khảo sát thành các quyết định kỹ thuật cụ thể:

| Insight từ khảo sát ($n=14$) | Quyết định thiết kế Prompt ([codebase/prompts/](file:///d:/Download/VINUNI%20AI/DAY5/K4-3B-E402-Latentia/codebase/prompts/)) | Áp dụng vào Golden Set ([eval/golden_set.json](file:///d:/Download/VINUNI%20AI/DAY5/K4-3B-E402-Latentia/eval/golden_set.json)) |
|---|---|---|
| **71.4% yêu cầu trả lời kèm nguồn; 45.5% bức xúc vì không biết nguồn gốc** | Bắt buộc mọi câu trả lời Happy Path và Domain Policy phải có dòng: `📌 Nguồn: #[kênh] (ngày/thông báo)`. Cấm hallucinate nguồn. | Tiêu chí cứng: 100% case có căn cứ phải có citation, nếu thiếu bị tính FAIL ngay. |
| **45.5% phàn nàn bot trả lời quá dài, làm loãng kênh** | Ràng buộc độ dài nghiêm ngặt: $\le 200$ ký tự (hoặc tối đa 3 câu ngắn). Cắt bỏ hoàn toàn câu chào hỏi rườm rà. | Runner kiểm tra độ dài $\le 200$ ký tự cho tất cả 24 test cases. |
| **54.5% học viên phàn nàn bot hỏi lại menu dài dòng (20.6% log tin nhắn)** | Thiết kế template `low_confidence.md` (HAX G10): Phát hiện câu hỏi mơ hồ, hỏi làm rõ súc tích kèm đúng 2 lựa chọn cụ thể (`Lab 02` vs `Milestone 1`). | Các test cases mơ hồ: `TC_12` ("Khi nào nộp bài?"), `TC_13` ("Mấy giờ hết hạn?"), `TC_14` ("Link bài học ở đâu?"). |
| **Quote "Toàn tag mod, mod ko trả lời" & 57.1% muốn chuyển TA khi không chắc** | Thiết kế template `no_grounding.md`: Khi dữ liệu không có căn cứ, bot thừa nhận trung thực và kích hoạt Handoff tag `@TA` kèm kênh `#ho-tro`. | Các test cases No-Grounding: `TC_09`, `TC_10`, `TC_11` cam kết 100% fallback sang TA, không đoán mò. |
| **35.7% cần rõ quy chế trừ điểm nộp muộn và điểm danh** | Thiết kế template `domain_policy.md`: Trích dẫn nguyên văn Mục 3.2 Quy chế (50%, 75%, 0 điểm) và lý do y tế. | Các test cases Domain Policy: `TC_18`, `TC_19`, `TC_20`. |

---

## 5. Kết luận & Đóng góp cho CP4

1. Dữ liệu khảo sát $n=14$ là cơ sở thực nghiệm vững chắc chứng minh **Pain Point có thật và nghiêm trọng**.
2. Thiết kế System Prompt và 5 Templates do Nguyễn Thị Vàng xây dựng giải quyết trực diện 3 nguyên nhân thất bại hàng đầu của bot cũ: **Thiếu nguồn (Grounding), Trả lời lan man (Conciseness), và Bịa đặt khi không biết (Hallucination)**.
3. Toàn bộ 14/24 cases trong Golden Set được trích xuất từ các câu hỏi thực tế của học viên trong khảo sát này, bảo đảm độ bao phủ (coverage) và tính thực tế cao nhất.
