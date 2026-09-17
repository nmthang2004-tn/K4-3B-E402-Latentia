# Canvas CP1 — B1 · Trợ lý Discord

## Thông tin nhóm
| Họ và Tên | Mã HV | Vai trò |
|---|---|---|
| Nguyễn Minh Thắng | 2A202602706 | Spec + Evidence |
| Nguyễn Thị Vàng | 2A202602897 | Prompt + Golden Set + Survey |
| Nguyễn Minh Tuấn | 2A202602420 | Build Prototype + Data Mining |


| # | Dòng | Nội dung |
|---|---|---|
| 1 | Track + đề | **B · B1 — Trợ lý Discord:** Trả lời tự động câu hỏi về lịch trình, deadline và tài liệu khoá học có căn cứ trích dẫn nguồn. |
| 2 | Job executor (ai · đang ở đâu · làm gì) | Học viên mới (tuần đầu), đang ở kênh chat Discord của khoá học, cần tra cứu gấp thông tin về deadline nộp bài, standup hoặc link tài liệu hướng dẫn. |
| 3 | Pain một câu (ai – đang làm gì – vướng đâu – hậu quả) | Học viên khi cần tra cứu deadline hoặc tài liệu bị trôi tin nhắn giữa hàng trăm thảo luận; hỏi bot hiện tại thì bot không hiểu ngữ cảnh hoặc trả lời lan man không nguồn, khiến học viên tốn nhiều thời gian và vẫn phải tag hỏi lại Teaching Assistant/Lab Coach. |
| 4 | 1–2 bằng chứng đầu (số + cách đếm + mã hội thoại/tin nhắn, hoặc khảo sát/phỏng vấn có số người) | • **Bằng chứng từ Data Pack (Data mining):**<br>&nbsp;&nbsp;1. *Vấn đề Logistics:* 142/306 câu hỏi gửi bot là về logistics (chiếm 46.4%). Bot không có dữ liệu thông báo chính thức nên trả lời *"không có thông tin"* và bảo học viên tự đi tìm ở 3 nguồn khác.<br>&nbsp;&nbsp;&nbsp;&nbsp;– *Cách đếm:* Lọc tin tag bot chứa từ khóa `deadline`, `hạn`, `nộp`, `link`, `ticket`, `form`, `xp`.<br>&nbsp;&nbsp;&nbsp;&nbsp;– *Mã tin minh họa:* `M07416` (hỏi hạn Lab02) → bot `M28485` không biết; `M56777` (hỏi hạn lập team) → bot `M02666` không biết; `M40677` (hỏi quy chế commit trễ) → bot `M00595`.<br>&nbsp;&nbsp;2. *Menu hỏi lại & Phản hồi dài:* 63/306 phản hồi của bot (20.6%) là menu hỏi lại dạng *"Bạn muốn hỏi trong ngữ cảnh nào?"*, khiến user phải gõ số cụt (1, 3, tất cả), sau đó bot tuôn phản hồi dài trung bình 486 ký tự (lên tới 1.238–1.864 ký tự) gây loãng kênh.<br>&nbsp;&nbsp;&nbsp;&nbsp;– *Cách đếm:* Lọc phản hồi bot có cụm *"ngữ cảnh nào / mô tả rõ hơn"*.<br>&nbsp;&nbsp;&nbsp;&nbsp;– *Mã tin minh họa:* `M49945` → bot `M36672` → user `M31100` → bot `M51292` (dài 1.238 ký tự).<br><br>• **Bằng chứng từ Khảo sát thực tế (n=14 học viên lớp 3B tuần đầu):**<br>&nbsp;&nbsp;1. *Khó khăn tra cứu:* 11/14 (78.6%) gặp khó khăn khi tìm deadline/lịch nộp bài; 8/14 (57.1%) từng gửi câu hỏi bị trùng lặp với người khác; 7/14 (50%) mất >3–5 phút hoặc không tìm được.<br>&nbsp;&nbsp;2. *Vấn đề với bot hiện tại:* 11/14 đã dùng bot nhưng 6/11 (54.5%) phản ánh bot không hiểu ngữ cảnh / trả lời xong vẫn phải hỏi lại TA; 10/14 (71.4%) yêu cầu bot trả lời chính xác kèm trích dẫn nguồn (quote: *"toàn tag mod, mod ko trả lời"*). |
| 5 | Lát cắt MỘT CÂU (1 user · 1 việc · 1 quyết định AI · 1 kết quả) | Học viên gõ câu hỏi tra cứu deadline/quy định vào Discord · AI đối soát câu hỏi với tài liệu thông báo chính thức để **quyết định câu hỏi có căn cứ xác thực hay không** · nếu có thì trả lời ngắn gọn kèm trích dẫn nguồn/link; nếu không đủ căn cứ thì nói rõ "chưa đủ căn cứ" và chuyển tiếp tag TA/Mod hỗ trợ. |
| 6 | AI tự làm đến đâu + 1 dòng lý do · ≥3 willing users ngoài nhóm | • **Tự làm:** Nhận câu hỏi, truy xuất thông báo/lịch trình chính thức, trích xuất câu trả lời kèm link/kênh nguồn.<br>• **Không tự làm:** Không bịa đặt khi thiếu căn cứ; không tự ý đưa ra quyết định thay đổi hạn nộp thay BTC.<br>• **Lý do:** 71.4% học viên cần câu trả lời có nguồn xác thực; sai sót về deadline/quy chế gây trễ bài nộp và mất điểm trực tiếp.<br>• **≥3 Willing users (ngoài nhóm, đã đồng ý test CP5):** Bùi Việt Anh, Hà Anh Tuấn, Trần Mạnh Hùng. |
| 7 | Phân công có tên | • **Nguyễn Minh Thắng (2A202602706):** Product Lead, Spec.md (§1–§6), evidence mining, video demo/pitch.<br>• **Nguyễn Thị Vàng (2A202602897):** Prompt engineering, grounding/retrieval, Golden Set (≥20 cases) & eval framework, khảo sát.<br>• **Nguyễn Minh Tuấn (2A202602420):** Prototype Discord Bot (API/LangChain), UI demo, kịch bản fallback & low-confidence, data mining. |

Bằng chứng ở dòng 4 có thể đến từ **data pack** (đếm được, có mã trích dẫn) hoặc **khảo sát / phỏng vấn** (ghi số người hỏi, số người gặp vấn đề, quote ngắn) — tốt nhất là cả hai.

---

## Phụ lục: Giải thích thuật ngữ (Glossary)

Bảng giải thích các thuật ngữ chuyên môn và từ viết tắt được sử dụng trong Canvas:

| Thuật ngữ / Viết tắt | Ý nghĩa trong ngữ cảnh Canvas |
|---|---|
| **CP (Checkpoint)** | Các mốc đánh giá tiến độ định kỳ của dự án (ví dụ: `CP1` chốt Canvas ý tưởng, `CP5` kiểm thử prototype với người dùng). |
| **Track B / B1** | Hướng đề tài xây dựng **Trợ lý Discord** hỗ trợ giải đáp thắc mắc cho học viên trong không gian học tập. |
| **Job executor** | Người trực tiếp thực hiện công việc (ở đây là *Học viên mới tuần đầu* cần tìm kiếm thông tin gấp trên Discord). |
| **Pain (Nỗi đau)** | Vấn đề, khó khăn người dùng gặp phải gây tốn thời gian hoặc dẫn đến hệ quả xấu (tin nhắn bị trôi, bot trả lời lan man/sai lệch, chờ đợi hỗ trợ lâu). |
| **Logistics** | Các câu hỏi liên quan đến vận hành khóa học: hạn nộp bài (deadline), lịch standup/họp, link tài nguyên, biểu mẫu (form), điểm thưởng (XP), ticket hỗ trợ. |
| **Data Pack / Data mining** | Bộ dữ liệu log tin nhắn Discord do khóa học cung cấp (`discord-pack`), được nhóm khai phá định lượng để lấy bằng chứng thực tế (mã tin nhắn dạng `M...`). |
| **Lát cắt (Thin Slice)** | Phạm vi giải pháp tối thiểu nhưng khép kín theo cấu trúc: *1 user · 1 việc · 1 quyết định AI · 1 kết quả*, giải quyết dứt điểm một trường hợp cốt lõi. |
| **Grounding / Căn cứ trích dẫn** | Cơ chế AI đối soát nội dung câu trả lời với tài liệu/thông báo chính thống từ Ban tổ chức, đảm bảo tính xác thực, không ảo giác (hallucination) và luôn kèm nguồn dẫn. |
| **Fallback & Low-confidence** | Kịch bản xử lý khi AI không tìm thấy tài liệu hoặc không đủ độ tự tin: bot thừa nhận *"chưa đủ căn cứ"* và chuyển tiếp (handoff) tag TA/Mod hỗ trợ, tuyệt đối không bịa đặt. |
| **Willing users** | Người dùng thật ngoài nhóm phát triển đã cam kết tham gia trải nghiệm và cung cấp phản hồi kiểm chứng cho prototype ở vòng test. |
| **Golden Set** | Bộ dữ liệu đối chuẩn gồm các trường hợp kiểm thử tiêu chuẩn (≥20 cases) dùng để đo lường độ chính xác của bot qua các lần cải tiến prompt/retrieval. |
| **TA / Lab Coach / Mod** | Lực lượng hỗ trợ vận hành và học thuật: Teaching Assistant (Trợ giảng), Lab Coach (Hướng dẫn thực hành) và Moderator (Điều phối viên Discord). |

