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
| 1 | Track + đề | |
| 2 | Job executor (ai · đang ở đâu · làm gì) | |
| 3 | Pain một câu (ai – đang làm gì – vướng đâu – hậu quả) | |
| 4 | 1–2 bằng chứng đầu (số + cách đếm + mã hội thoại/tin nhắn, hoặc khảo sát/phỏng vấn có số người) | • **Bằng chứng 1 (Logistics):** 142/306 câu hỏi gửi bot là về logistics (chiếm 46.4%). Bot không có dữ liệu thông báo chính thức nên trả lời *"không có thông tin"* và bảo học viên tự đi tìm ở 3 nguồn khác.<br>- *Cách đếm:* Lọc tin tag bot chứa từ khóa `deadline`, `hạn`, `nộp`, `link`, `ticket`, `form`, `xp`.<br>- *Mã tin minh họa:* `M07416` (hỏi hạn Lab02) → bot `M28485` không biết; `M56777` (hỏi hạn lập team) → bot `M02666` không biết; `M40677` (hỏi quy chế commit trễ) → bot `M00595`.<br><br>• **Bằng chứng 2 (Menu hỏi lại & phản hồi dài):** 63/306 phản hồi của bot (20.6%) là menu hỏi lại dạng *"Bạn muốn hỏi trong ngữ cảnh nào?"*, khiến user phải gõ số cụt (1, 3, tất cả), sau đó bot tuôn phản hồi dài trung bình 486 ký tự (lên tới 1.238–1.864 ký tự) gây loãng kênh.<br>- *Cách đếm:* Lọc phản hồi bot có cụm *"ngữ cảnh nào / mô tả rõ hơn"*.<br>- *Mã tin minh họa:* `M49945` → bot `M36672` → user `M31100` → bot `M51292` (dài 1.238 ký tự). |
| 5 | Lát cắt MỘT CÂU (1 user · 1 việc · 1 quyết định AI · 1 kết quả) | |
| 6 | AI tự làm đến đâu + 1 dòng lý do · ≥3 willing users ngoài nhóm | |
| 7 | Phân công có tên | |

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