# Canvas CP1 — B1 · Trợ lý Discord

## Thông tin nhóm
| Họ và Tên | Mã HV | Vai trò |
|---|---|---|
| Nguyễn Minh Thắng | 2A202602706 | Spec + Evidence |
| Nguyễn Thị Vàng | 2A202602897 | Prompt + Golden Set+Khảo sát |
| Nguyễn Minh Tuấn | 2A202602420 | Build Prototype |

# Ví dụ Canvas 7 dòng (CP1)

Canvas nộp ở CP1 theo scaffold `02-guide.md` §1.5 — mỗi dòng một ý, cả canvas vừa một trang. Dưới đây là 3 bài của các nhóm khoá trước (đã ẩn tên, chỉnh nhẹ), kèm ghi chú vì sao đạt. Số liệu trong ví dụ viết dạng `XX/XXX` — nhóm bạn phải tự đếm trên `data/` của khoá này và ghi số thật.

## Mẫu trống — copy vào `canvas.md` của repo nhóm

| # | Dòng | Nội dung |
|---|---|---|
| 1 | Track + đề | **B · B1 — Trợ lý Discord:** Trả lời tự động câu hỏi về lịch trình, deadline và tài liệu khoá học có căn cứ trích dẫn nguồn. |
| 2 | Job executor (ai · đang ở đâu · làm gì) | Học viên mới (tuần đầu), đang ở kênh chat Discord của khoá học, cần tra cứu gấp thông tin về deadline nộp bài, standup hoặc link tài liệu hướng dẫn. |
| 3 | Pain một câu (ai – đang làm gì – vướng đâu – hậu quả) | Học viên khi cần tra cứu deadline hoặc tài liệu bị trôi tin nhắn giữa hàng trăm thảo luận; hỏi bot hiện tại thì bot không hiểu ngữ cảnh hoặc trả lời lan man không nguồn, khiến học viên tốn nhiều thời gian và vẫn phải tag hỏi lại TA. |
| 4 | 1–2 bằng chứng đầu (số + cách đếm + mã hội thoại/tin nhắn, hoặc khảo sát/phỏng vấn có số người) | • **Bằng chứng từ Data Pack (Data mining):**<br>&nbsp;&nbsp;1. *Vấn đề Logistics:* 142/306 câu hỏi gửi bot là về logistics (chiếm 46.4%). Bot không có dữ liệu thông báo chính thức nên trả lời *"không có thông tin"* và bảo học viên tự đi tìm ở 3 nguồn khác.<br>&nbsp;&nbsp;&nbsp;&nbsp;– *Cách đếm:* Lọc tin tag bot chứa từ khóa `deadline`, `hạn`, `nộp`, `link`, `ticket`, `form`, `xp`.<br>&nbsp;&nbsp;&nbsp;&nbsp;– *Mã tin minh họa:* `M07416` (hỏi hạn Lab02) → bot `M28485` không biết; `M56777` (hỏi hạn lập team) → bot `M02666` không biết; `M40677` (hỏi quy chế commit trễ) → bot `M00595`.<br>&nbsp;&nbsp;2. *Menu hỏi lại & Phản hồi dài:* 63/306 phản hồi của bot (20.6%) là menu hỏi lại dạng *"Bạn muốn hỏi trong ngữ cảnh nào?"*, khiến user phải gõ số cụt (1, 3, tất cả), sau đó bot tuôn phản hồi dài trung bình 486 ký tự (lên tới 1.238–1.864 ký tự) gây loãng kênh.<br>&nbsp;&nbsp;&nbsp;&nbsp;– *Cách đếm:* Lọc phản hồi bot có cụm *"ngữ cảnh nào / mô tả rõ hơn"*.<br>&nbsp;&nbsp;&nbsp;&nbsp;– *Mã tin minh họa:* `M49945` → bot `M36672` → user `M31100` → bot `M51292` (dài 1.238 ký tự).<br><br>• **Bằng chứng từ Khảo sát thực tế (n=14 học viên lớp 3B tuần đầu):**<br>&nbsp;&nbsp;1. *Khó khăn tra cứu:* 11/14 (78.6%) gặp khó khăn khi tìm deadline/lịch nộp bài; 8/14 (57.1%) từng gửi câu hỏi bị trùng lặp với người khác; 7/14 (50%) mất >3–5 phút hoặc không tìm được.<br>&nbsp;&nbsp;2. *Vấn đề với bot hiện tại:* 11/14 đã dùng bot nhưng 6/11 (54.5%) phản ánh bot không hiểu ngữ cảnh / trả lời xong vẫn phải hỏi lại TA; 10/14 (71.4%) yêu cầu bot trả lời chính xác kèm trích dẫn nguồn (quote: *"toàn tag mod, mod ko trả lời"*). |
| 5 | Lát cắt MỘT CÂU (1 user · 1 việc · 1 quyết định AI · 1 kết quả) | Học viên gõ câu hỏi tra cứu deadline/quy định vào Discord · AI đối soát câu hỏi với tài liệu thông báo chính thức để **quyết định câu hỏi có căn cứ xác thực hay không** · nếu có thì trả lời ngắn gọn kèm trích dẫn nguồn/link; nếu không đủ căn cứ thì nói rõ "chưa đủ căn cứ" và chuyển tiếp tag TA/Mod hỗ trợ. |
| 6 | AI tự làm đến đâu + 1 dòng lý do · ≥3 willing users ngoài nhóm | • **Tự làm:** Nhận câu hỏi, truy xuất thông báo/lịch trình chính thức, trích xuất câu trả lời kèm link/kênh nguồn.<br>• **Không tự làm:** Không bịa đặt khi thiếu căn cứ; không tự ý đưa ra quyết định thay đổi hạn nộp thay BTC.<br>• **Lý do:** 71.4% học viên cần câu trả lời có nguồn xác thực; sai sót về deadline/quy chế gây trễ bài nộp và mất điểm trực tiếp.<br>• **≥3 Willing users (ngoài nhóm, đã đồng ý test CP5):** Đào Hải Long, Vũ Hoàng Nam, Trần Quốc Bảo. |
| 7 | Phân công có tên | • **Nguyễn Minh Thắng (2A202602706):** Product Lead, Spec.md (§1–§6), evidence mining & khảo sát, video demo/pitch.<br>• **Nguyễn Thị Vàng (2A202602897):** Prompt engineering, grounding/retrieval, Golden Set (≥20 cases) & eval framework.<br>• **Nguyễn Minh Tuấn (2A202602420):** Prototype Discord Bot (API/LangChain), UI demo, kịch bản fallback & low-confidence. |

Bằng chứng ở dòng 4 có thể đến từ **data pack** (đếm được, có mã trích dẫn) hoặc **khảo sát / phỏng vấn** (ghi số người hỏi, số người gặp vấn đề, quote ngắn) — tốt nhất là cả hai.


## Mẫu 3 · Track B — trợ lý Discord

1. **Track + đề:** B · Trợ lý Discord — trả lời câu hỏi tiện ích lặp lại.
2. **Job executor:** Học viên mới, tuần đầu, đang ở kênh chung, vừa gõ một câu hỏi về tiện ích (căn tin, thư viện, thẻ, wifi).
3. **Pain:** Câu hỏi bị trôi giữa tin nhắn khác, không ai trả lời hoặc trả lời sau vài giờ; học viên hỏi lại hoặc tự đi tìm, cùng một câu được hỏi nhiều lần.
4. **Bằng chứng đầu:**
   - Trong `discord-pack/k4_messages.csv`, `XX/X.XXX` tin là câu hỏi tiện ích (lọc từ khoá "căn tin | thư viện | thẻ | wifi | gửi xe" + dấu "?"); `XX` trong số đó không có reply trong 2 giờ. *Mã tin minh hoạ:* `D0XXX`, `D0XXX`, `D0XXX`.
   - Hỏi `XX` học viên trong lớp: `XX/XX` từng hỏi một câu tiện ích trên Discord mà không được trả lời; `XX/XX` cuối cùng đi hỏi trực tiếp coach.
5. **Lát cắt:** Học viên mới gõ câu hỏi tiện ích vào kênh chung · AI quyết định câu hỏi có khớp mục nào trong tài liệu nội quy/tiện ích không · nếu khớp thì trả lời kèm trích dẫn mục; nếu không thì nói "chưa có trong tài liệu" và tag người phụ trách.
6. **AI tự làm đến đâu:** *Tự* trả lời khi tìm được mục khớp; *không tự* suy đoán, *không tự* tạo event/poll thay người dùng. *Lý do:* thông tin sai về nội quy làm học viên vi phạm; tạo event thay mặt người khác là hành động không hoàn tác được. **Willing users:** `[Tên 1]`, `[Tên 2]`, `[Tên 3]`.
7. **Phân công:** `[Tên A]` — evidence + golden set · `[Tên B]` — prompt/retrieval · `[Tên C]` — bot + AI call · `[Tên D]` — spec + demo · `[Tên E]` — user test + changelog.

> **Vì sao đạt:** dòng 2 là *một vai đang làm một việc*, không phải "học viên nói chung". Dòng 4 đếm được trên Discord pack và có mã tin để TA mở ra xem. Dòng 5 chỉ có **một** việc (trả lời câu hỏi tiện ích) — không gộp thêm "gom nhóm đá bóng" dù ý tưởng ban đầu có; phần đó để backlog. Dòng 6 nói rõ AI không hành động thay người dùng.

---

*Chỉnh sửa từ bài nộp của các nhóm khoá trước, đã ẩn tên và thay số liệu bằng `XX`. Số thật do nhóm bạn tự đếm.*