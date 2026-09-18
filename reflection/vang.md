# BẢN REFLECTION CÁ NHÂN (INDIVIDUAL REFLECTION) — CP5

> **Họ và Tên:** Nguyễn Thị Vàng  
> **Mã học viên:** 2A202602897  
> **Vai trò trong nhóm:** Prompt Engineering, Grounding/UX, Golden Set & Evaluation Framework Lead  
> **Dự án:** Trợ lý Discord hỗ trợ học viên (Track B1) · Nhóm Latentia (K4-3B-E402 · Cụm C1)  
> **Thời điểm hoàn thành:** 18/09/2026 (Checkpoint 5 — Hoàn tất hồ sơ dự án)

---

## 1. Tổng quan vai trò & Phạm vi đảm nhiệm xuyên suốt dự án

Trong hành trình 39 giờ của Mini Hackathon AI Batch 04, tôi đảm nhận vai trò **Prompt Engineering & Evaluation Lead** — vị trí chịu trách nhiệm chính về chất lượng đầu ra của AI, kiến trúc tương tác người - máy (UX/HAX), thiết kế bộ tiêu chuẩn kiểm thử (Golden Set) và kiểm chứng thực địa với người dùng thật.

Dự án của nhóm Latentia không định vị là một "chatbot AI biết tuốt" thông thường, mà là một **sản phẩm AI có trách nhiệm (Responsible AI)** phục vụ trực tiếp cho các học viên tuần đầu lớp K4-3B đang đối mặt với sự quá tải thông tin và nguy cơ lỡ deadline. Xuyên suốt từ CP1 đến CP5, tôi đã trực tiếp chịu trách nhiệm và hoàn thành các đầu việc cốt lõi sau:

1. **Khảo sát thực nghiệm & Bằng chứng thực địa ($n=14$):** Thiết kế biểu mẫu, phân tích định lượng và trích xuất insights từ 14 học viên lớp 3B ([`eval/survey_analysis.md`](../eval/survey_analysis.md)), chuyển hóa nỗi đau của người dùng thành các ràng buộc kỹ thuật.
2. **Kiến trúc System Prompt & 5 Templates chuyên biệt:** Trực tiếp thiết kế System Prompt và 5 prompt templates theo triết lý Zero Hallucination, ràng buộc độ dài $\le 200$ ký tự, bắt buộc trích dẫn nguồn `📌 Nguồn: #[kênh]` và định tuyến theo 4 đường đi trải nghiệm ([`codebase/prompts/`](../codebase/prompts/)).
3. **Xây dựng Golden Set 24 cases chuẩn mực:** Thiết kế 24 test cases bao phủ trọn vẹn 4 lớp chỗ khó (HAX Playbook/PAIR), trong đó có 14/24 cases (58.3%) được trích xuất trực tiếp từ các câu hỏi có thật của học viên ([`eval/golden_set.json`](../eval/golden_set.json)).
4. **Phân tích lỗi (Error Analysis) & Tinh chỉnh qua các lượt đo:** Trực tiếp phân tích 13 ca lỗi ở Run 1 (đạt 45.8%), tái cấu trúc prompt logic và ambiguity gate để đưa Run 2 đạt tuyệt đối 24/24 (100.0%) vượt qua Quality Bar đã khóa cứng ([`eval/analysis.md`](../eval/analysis.md)).
5. **Thực hiện vòng User Validation CP5:** Trực tiếp liên hệ và điều phối 3 phiên kiểm thử người dùng (10 phút/người) với 3 willing users ngoài nhóm, ghi nhận hành vi, thu thập quote nguyên văn và hoàn thiện log nghiệm thu ([`validation/feedback_log.md`](../validation/feedback_log.md)).

---

## 2. Những bước ngoặt tư duy & Bài học lớn nhất (Key Learnings)

Qua quá trình trực tiếp xây dựng prompt và đánh giá sản phẩm AI, tôi đã rút ra được 4 bài học mang tính thay đổi tư duy sâu sắc:

### 2.1. "Look at your data" — Sự thật nằm ở output thô, không nằm ở kỳ vọng trừu tượng
Trước khi bước vào lab thực hành, tôi từng nghĩ prompt engineering là việc trau chuốt ngôn từ hoa mỹ. Nhưng khi bắt tay vào thực tế, bài học lớn nhất mà tôi học được từ Hamel Husain và hướng dẫn của khóa học là: **phải nhìn thẳng vào dữ liệu thô**. 
Khi chạy thử nghiệm đầu tiên với dữ liệu thật, tôi nhận ra học viên không hỏi những câu hoàn chỉnh như trong sách giáo khoa; họ hỏi bằng teencode ("khi lào nộp"), câu hỏi cụt ("link?"), hoặc những câu hỏi ghép nhiều ý ("vắng standup có bị trừ điểm không và gửi giấy khám ở đâu?"). Nếu không đọc 306 dòng chatlog Discord và phân tích 14 câu trả lời khảo sát, tôi sẽ không bao giờ lường trước được rằng: **54.5% học viên bức xúc vì bot cũ hỏi lại bằng menu quá dài**, và **45.5% mất niềm tin vì không biết thông tin lấy từ đâu**. Mọi dòng prompt tôi viết sau đó đều bắt nguồn từ chính những output tệ hại đã quan sát được.

### 2.2. Quality Bar phải được khóa cứng trước khi đo lường (Avoid moving the goalposts)
Khoảnh khắc thử thách nhất đối với tôi trong dự án là sáng ngày 18/9, khi chạy lượt đo đầu tiên (Run 1) của mô hình AI thật qua API Gemini: **kết quả chỉ đạt 11/24 cases (45.8%)**. 
Cảm giác lúc đó rất lo lắng vì deadline CP4 đang đến gần. Tâm lý thông thường sẽ là: *"Hay là mình nới lỏng tiêu chí? Hay là mình hạ Quality Bar từ 85% xuống 60% để báo cáo cho đẹp?"*. Nhưng nhóm chúng tôi đã kiên quyết tuân thủ nguyên tắc: **Quality Bar đã cam kết tại CP4 là bất di bất dịch (≥85% tổng thể, 100% No-Grounding không bịa, 100% có trích dẫn nguồn)**. 
Chính việc giữ nguyên "thanh xà" đó đã buộc tôi phải ngồi lại, mổ xẻ từng case trong số 13 case thất bại:
- Tôi phát hiện ra ở Lớp ② (Low-confidence), bộ điều phối prompt đang ưu tiên tìm tài liệu (retrieval) trước khi kiểm tra tính mơ hồ (ambiguity gate), khiến bot đoán mò deadline thay vì hỏi lại.
- Ở Lớp ① (No-grounding), bot có xu hướng suy diễn từ một quy chế gần nghĩa thay vì kích hoạt mẫu fallback tag @TA.
Nhờ phân tích có hệ thống thay vì sửa chữa chắp vá, tôi đã tái cấu trúc lại bộ template, bổ sung mapping ngữ cảnh và đạt kết quả 24/24 (100%) ở Run 2 một cách hoàn toàn trung thực và thuyết phục.

### 2.3. Chi phí sai sót (Cost-of-Error) quyết định mức độ tự động hóa
Một quyết định thiết kế quan trọng mà tôi cùng anh Thắng và Tuấn tranh luận rất kỹ ở CP1 và CP2 là: *Nên để bot tự động trả lời (Automate) hay chỉ hỗ trợ (Conditional/Augment)?*
Trong bối cảnh khóa học công nghệ khắc nghiệt như AI20k, nếu bot cung cấp sai một mốc deadline nộp bài (ví dụ thông báo hạn là 23:59 ngày 21/9 trong khi hạn thật là ngày 20/9), học viên sẽ bị hệ thống trừ điểm trực tiếp hoặc trượt checkpoint. **Chi phí của một lỗi sai (Cost-of-Error) là cực kỳ đắt đỏ**. 
Do đó, chúng tôi dứt khoát chọn cơ chế **Conditional Automation**:
- Khi có căn cứ chắc chắn trong thông báo chính thức $\rightarrow$ AI tự động trả lời ngắn gọn kèm nguồn.
- Khi không có căn cứ hoặc dữ liệu cá nhân $\rightarrow$ AI dừng lại, dũng cảm nói *"chưa tìm thấy thông tin"* và kích hoạt luồng bàn giao (Handoff) cho TA/Mod.
Hành vi này đã được chứng minh là hoàn toàn đúng đắn khi đem ra thử nghiệm với 3 willing users ở CP5: người dùng cảm thấy an tâm tuyệt đối vì bot không bao giờ "bịa đặt" (hallucinate).

### 2.4. Nguyên tắc HAX G10 — Sự dũng cảm nói "tôi không biết"
Nguyên tắc Microsoft HAX G10 (*Thu hẹp phạm vi khi nghi ngờ*) là kim chỉ nam cho toàn bộ thiết kế prompt của tôi. Một AI giỏi không phải là AI cố gắng trả lời mọi câu hỏi, mà là AI biết rõ ranh giới thẩm quyền của mình. Trong prompt `no_grounding.md` và `out_of_scope.md`, tôi đã cài đặt các "bộ phanh an toàn" (safety guardrails): kiên quyết từ chối viết code giải bài tập, không can thiệp vào điểm danh cá nhân và từ chối các tin đồn chưa được kiểm chứng. Điều này biến bot thành một trợ lý đáng tin cậy thay vì một công cụ gây nhiễu loạn kênh học tập.

---

## 3. Những khó khăn kỹ thuật đã vượt qua & Cách giải quyết

Trong quá trình thực thi, tôi đã đối mặt với 3 thách thức kỹ thuật cụ thể:

| Thách thức kỹ thuật | Tác động ban đầu | Giải pháp kỹ thuật đã áp dụng |
|---|---|---|
| **Giới hạn Rate Limit của Gemini Free Tier (15 RPM)** | Khi chạy bộ test 24 cases tự động bằng script Python, request thứ 16 liên tục bị ngắt kết nối với lỗi HTTP 429 (`ResourceExhausted`). | Phối hợp cùng Tuấn cấu hình cơ chế sleep giãn cách 5 giây giữa các lượt gọi API trong `eval/run_eval.py`, bổ sung retry logic với exponential backoff. |
| **Xung đột Matcher giữa Tiêu chí đánh giá và Ngôn ngữ tự nhiên** | Một số case như `TC_06` bot trả lời đúng ý *"không gửi file zip"* nhưng bị runner chấm FAIL vì bộ lọc chứa từ cấm `file zip` trong `must_not_contain`. | Tinh chỉnh lại logic assertion: chuyển từ kiểm tra substring máy móc sang kiểm tra ngữ nghĩa (semantic intent) và phân tách rõ giữa hành vi khuyến nghị với cảnh báo cấm. |
| **Độ dài phản hồi làm loãng kênh chat** | LLM mặc định có xu hướng chào hỏi khách sáo dài dòng ("Chào bạn, tôi rất vui được hỗ trợ..."), vi phạm pain point của học viên. | Cài đặt chỉ thị cứng trong System Prompt: *"Cấm hoàn toàn câu chào hỏi rườm rà. Bắt đầu ngay bằng câu trả lời. Giới hạn nghiêm ngặt $\le 200$ ký tự hoặc tối đa 3 ý ngắn."* |

---

## 4. Tự đánh giá hạn chế & Nếu có thêm 1 tuần sẽ làm gì?

Dù đã đạt được 100% mục tiêu của các checkpoint, nhìn nhận một cách khắt khe dưới góc độ Product & UX, tôi nhận thấy sản phẩm vẫn còn những điểm có thể làm tốt hơn:

1. **Chuyển đổi từ Prompt-injected Context sang Dynamic RAG:** Hiện tại, tài liệu thông báo và quy chế được nạp tĩnh thông qua context của prompt. Nếu có thêm thời gian, tôi sẽ cùng nhóm xây dựng một pipeline RAG hoàn chỉnh (sử dụng ChromaDB hoặc FAISS) kết hợp bộ lọc Metadata theo ngày, giúp bot tự động cập nhật ngay khi kênh `#thong-bao` có tin nhắn mới mà không cần cập nhật prompt thủ công.
2. **Tích hợp Discord Interactive Components:** Phản hồi từ bạn Hà Anh Tuấn ở phiên validation CP5 chỉ ra rằng việc gõ lại chữ để làm rõ câu hỏi mơ hồ vẫn tạo ra một chút ma sát (friction). Tôi muốn nâng cấp template Low-confidence để trả về Discord Buttons hoặc Dropdown Menu, cho phép người dùng bấm chọn trực tiếp chỉ bằng một cú click chuột.
3. **Cơ chế Handoff thông minh hơn:** Khi kích hoạt nhánh No-Grounding, thay vì chỉ hướng dẫn học viên tag `@TA`, bot có thể tự động tạo một Ticket riêng trong kênh hỗ trợ và đính kèm ngữ cảnh câu hỏi để trợ giảng nắm bắt ngay vấn đề.

---

## 5. Đánh giá sự phối hợp nhóm (Team Collaboration)

Tôi cảm thấy vô cùng may mắn và tự hào khi được đồng hành cùng hai đồng đội trong nhóm Latentia:
- **Nguyễn Minh Thắng (Product Lead):** Người giữ vững tầm nhìn sản phẩm, luôn nhắc nhở cả nhóm không đi chệch khỏi "lát cắt một câu", quản lý spec chặt chẽ và chỉ huy nhịp độ các checkpoint rất chuyên nghiệp.
- **Nguyễn Minh Tuấn (Engineering Lead):** Người biến các ý tưởng thiết kế prompt của tôi thành code chạy thật trên Discord, hỗ trợ tích cực trong việc xây dựng runner và xử lý lỗi hệ thống trong đêm.

Sự phân công rõ ràng, tôn trọng chuyên môn của nhau và tinh thần phản biện thẳng thắn dựa trên số liệu thực tế đã giúp nhóm Latentia hoàn thành dự án đúng hạn, chuẩn xác và không hề có sự thỏa hiệp về chất lượng.

---

## 6. Lời kết

Mini Hackathon AI không chỉ là một bài tập học thuật, mà là một trải nghiệm thực chiến vô giá giúp tôi thấu hiểu trọn vẹn vòng đời của một sản phẩm AI: từ việc đi tìm nỗi đau có thật của người dùng, chấp nhận sự vụng về của những phiên bản đầu tiên, kiên định với thanh đo chất lượng, cho đến niềm hạnh phúc khi thấy người dùng thật thở phào nhẹ nhõm khi sử dụng sản phẩm. Tôi tin rằng tư duy lấy người dùng làm trung tâm và tính kỷ luật trong đánh giá AI (Evaluation Discipline) sẽ là hành trang quý giá nhất theo tôi trong suốt sự nghiệp công nghệ sau này.
