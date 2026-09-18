# AI SPEC — Trợ lý Discord · Nhóm Latentia · Zone C1

> **Track:** B1 — Trợ lý Discord
> **Loại:** Tính năng mới

---

## §1. User & Job

- **Job executor:** Học viên mới (tuần đầu), đang ở kênh chat Discord của khoá học, cần tra cứu gấp thông tin về deadline nộp bài, standup hoặc link tài liệu hướng dẫn.
- **Core JTBD:** Khi đang ở kênh Discord và cần tra cứu thông tin khoá học, tôi muốn được trả lời ngay có trích dẫn nguồn, để không phải tự tìm kiếm giữa hàng trăm tin nhắn hoặc tag hỏi TA.
- **Problem statement:** Học viên khi cần tra cứu deadline hoặc tài liệu bị trôi tin nhắn giữa hàng trăm thảo luận; hỏi bot hiện tại thì bot không hiểu ngữ cảnh hoặc trả lời lan man không nguồn, khiến học viên tốn nhiều thời gian và vẫn phải tag hỏi lại TA.
- **Evidence A — định lượng:**
  - Mining (khoá K4): 142/306 câu hỏi gửi bot là về logistics (46.4%); 63/306 phản hồi (20.6%) là menu hỏi lại dài.
  - Khảo sát (n=14): 11/14 (78.6%) gặp khó khăn tìm deadline; 10/14 (71.4%) yêu cầu trả lời có trích dẫn nguồn. Chi tiết phân tích khảo sát do Vàng chủ trì: [`eval/survey_analysis.md`](eval/survey_analysis.md).
- **Evidence B — định tính, quote nguyên văn từ CSV khảo sát ngày 17/09/2026:**
  - *"Câu trả lời ko có ích, toàn tag mod, mod ko trả lời."* — phản hồi 17/09/2026 18:51:59.
  - *"Trả lời quá dài, không biết câu trả lời lấy từ đâu, trả lời nhưng tôi vẫn phải hỏi TA"* — phản hồi 17/09/2026 18:36:32.
  - *"Nói rõ rằng bot không chắc chắn và đưa nguồn để tôi tự kiểm tra"* — phản hồi ở câu hỏi xử lý khi không chắc chắn.
  - *"Trả lời chính xác hơn và kèm nguồn"* — phản hồi về cải thiện ưu tiên.
  - *"Tự phát hiện câu hỏi đã được hỏi trước đó"* — phản hồi về cải thiện ưu tiên.
  - Các quote được đối chiếu trong [`eval/survey_analysis.md`](eval/survey_analysis.md) và file CSV khảo sát trong repository.

---

## §2. Impact & quyết định chọn

- **Bảng impact:**

| Ứng viên | Người gặp | Tần suất | Tốn gì | Build nổi? | Chọn? |
|----------|-----------|---------|---------|------------|-------|
| Tra cứu deadline/tài liệu | 11/14 (78.6%) | 2-3 lần/tuần | 3-10 phút + frustration | ✅ | ✅ |
| Hỏi lại TA cùng câu hỏi | 8/14 (57.1%) | Thỉnh thoảng | Tốn thời gian TA | ✅ | |
| Bot trả lời dài/loãng kênh | 6/11 (54.5%) | Thường xuyên | Khó theo dõi | ⚠️ | |

- **Ứng viên loại:** Gom nhóm đá bóng, tạo poll/event — không build trong scope này.
- **Chọn:** Tra cứu deadline/tài liệu với trích dẫn nguồn — pain rõ ràng, bằng chứng mạnh, build nổi.
- **Lý do loại các ứng viên còn lại:** Hỏi lại TA là hậu quả cần giảm chứ chưa phải lát cắt sản phẩm chính; bot trả lời dài là triệu chứng của việc thiếu grounding và có thể xử lý trong giải pháp đã chọn; poll/event nằm ngoài non-goals và không phục vụ JTBD tra cứu thông tin.

---

## §3. Giải pháp tương tự đã nghiên cứu

- **ChatGPT (free):**
  - Flow: Hỏi → trả lời ngay
  - Học: Luôn trả lời nhanh, không hỏi lại
  - Né: Không có trích dẫn nguồn, có thể bịa thông tin
  - Khác: Bot Discord chỉ trả lời khi có căn cứ trong tài liệu chính thức

- **Bot Discord hiện tại:**
  - Flow: Hỏi → menu hỏi lại → trả lời dài
  - Học: Cố gắng tìm ngữ cảnh
  - Né: Trả lời không có nguồn, gây loãng kênh
  - Khác: Chỉ trả lời có căn cứ, chuyển TA khi không biết

---

## §4. Thiết kế

- **Lát cắt MỘT CÂU:** Học viên gõ câu hỏi tra cứu deadline/quy định vào Discord · AI đối soát câu hỏi với tài liệu thông báo chính thức để **quyết định câu hỏi có căn cứ xác thực hay không** · nếu có thì trả lời ngắn gọn kèm trích dẫn nguồn/link; nếu không đủ căn cứ thì nói rõ "chưa đủ căn cứ" và chuyển tiếp tag TA/Mod hỗ trợ.

- **Non-goals:**
  1. Không trả lời câu hỏi kiến thức chung (hỏi code, hỏi bài tập)
  2. Không thay đổi deadline/quy chế thay BTC
  3. Không tạo event/poll thay người dùng
  4. Không nhắn tin nhắc nhở tự động

- **Mức prototype:** Mock — flow bấm được, data giả, AI call thật ở lõi trả lời

- **Automation: Conditional**
  - *Lý do (cost-of-error):* Sai deadline khiến học viên mất điểm trực tiếp (đắt) → AI chỉ trả lời khi có căn cứ trong tài liệu; không đủ căn cứ → chuyển TA (người chịu trách nhiệm). Không dùng Automate vì sai thì đắt; không dùng Augment vì học viên cần trả lời ngay, không chờ TA duyệt.

- **§4b. Nguyên tắc HAX/PAIR đã áp dụng:**

| Nguyên tắc | Mã | Áp dụng vào đâu trong prototype |
|-------------|-----|----------------------------------|
| Thu hẹp phạm vi khi nghi ngờ | G10 (bắt buộc) | Khi câu hỏi mơ hồ ("khi nào nộp?") → bot hỏi lại: "Bạn đang hỏi về Lab hay Project?" |
| Giải thích vì sao | G11 | Bot trả lời kèm: "Theo thông báo ngày XX, link: ..." |
| Sửa dễ dàng | G9 | Nút "Sửa kết quả" / "Thử lại" ngay dưới mỗi câu trả lời |
| Gạt bỏ dễ dàng | G8 | User có thể bỏ qua câu trả lời, gõ câu hỏi khác ngay |
| Làm rõ hệ thống làm được gì | G1 | Tin nhắn chào khi bot được mention: "Mình là Trợ lý Discord — hỏi về deadline, lịch, link tài liệu nhé!" |

- **§4c. Thiết kế System Prompt & Prompt Templates (Phụ trách: Nguyễn Thị Vàng - 2A202602897):**
  - **System Prompt Outline:** Định nghĩa rõ vai trò Trợ lý Discord lớp K4-3B; giới hạn trả lời thông tin vận hành; cấm tuyệt đối viết code/giải bài tập (Non-goals); ràng buộc Zero Hallucination (chỉ dùng `[CONTEXT_DATA]`), độ dài $\le 200$ ký tự, và bắt buộc đính kèm `📌 Nguồn: #[kênh]`. Chi tiết: [`codebase/prompts/system.md`](codebase/prompts/system.md).
  - **Prompt Templates cho 4 đường đi:**
    1. *Happy Path:* Trả lời trực tiếp kèm trích dẫn nguồn và nút sửa/tag TA. Chi tiết: [`codebase/prompts/templates/happy_path.md`](codebase/prompts/templates/happy_path.md).
    2. *Low-Confidence (G10):* Phát hiện câu hỏi mơ hồ, cấm đoán mò, hỏi làm rõ kèm 2-3 lựa chọn mốc cụ thể. Chi tiết: [`codebase/prompts/templates/low_confidence.md`](codebase/prompts/templates/low_confidence.md).
    3. *No-Grounding (G10/PAIR):* Thiếu căn cứ thì thừa nhận chưa có dữ liệu và kích hoạt cơ chế Handoff tag @TA. Chi tiết: [`codebase/prompts/templates/no_grounding.md`](codebase/prompts/templates/no_grounding.md).
    4. *Out-of-Scope (G1):* Lịch sự từ chối giải bài/viết code và hướng dẫn sang kênh `#thao-luan`. Chi tiết: [`codebase/prompts/templates/out_of_scope.md`](codebase/prompts/templates/out_of_scope.md).
    5. *Domain Policy (G11/G2):* Quy chế đặc thù (nộp muộn, vắng standup, commit timestamp) trích dẫn điều khoản chính xác. Chi tiết: [`codebase/prompts/templates/domain_policy.md`](codebase/prompts/templates/domain_policy.md).
  - **Báo cáo kiểm thử 5 cases:** Đã thẩm định đạt 5/5 cases (100.0%) tại [`codebase/prompts/prompt_test_report.md`](codebase/prompts/prompt_test_report.md).

---

## §5. Kiểu lỗi — 4 lớp chỗ khó + kịch bản

| Lớp | Tình huống | Hành vi mong đợi | Nguyên tắc |
|------|-----------|-----------------|------------|
| ① Nguồn sự thật | Hỏi deadline không có trong tài liệu | Bot: "Mình chưa tìm thấy thông tin này. Tag @TA nhé!" | G10 |
| ② Mơ hồ/thiếu | "Khi nào nộp?" (không rõ Lab/Project) | Bot: "Bạn đang hỏi về deadline nộp bài nào?" | G10 |
| ③ Ngoài phạm vi | "Viết code giùm tôi" | Bot: "Mình chỉ hỗ trợ tra cứu thông tin khoá học. Câu hỏi về code, bạn hỏi TA nhé!" | G1 |
| ④ Đặc thù domain | Hỏi quy chế commit trễ | Bot: "Theo quy định khoá học: [trích dẫn]. Chi tiết: [link]" | G11 |

**Ma trận kịch bản nghiệm thu (10 kịch bản, mỗi kịch bản một dòng):**

| Tình huống | Lớp | Hành vi mong muốn | Nguyên tắc áp dụng |
|---|---|---|---|
| Hạn nộp Lab02 là khi nào? | Happy Path | Trả lời đúng deadline và kèm nguồn | G11 |
| Deadline Project cuối kỳ có thay đổi không? | ① No-Grounding | Không đoán; nói chưa có thông tin và chuyển @TA | G10/PAIR Handoff |
| Khi nào nộp? | ② Low-Confidence | Hỏi lại Lab 02 hay Milestone 1 Project | G10 |
| Viết code Python giùm | ③ Out-of-Scope | Từ chối, nêu phạm vi và hướng sang #thao-luan | G1 |
| Quy chế commit trễ thế nào? | ④ Domain Policy | Trả lời theo quy chế và kèm nguồn | G11 |
| XP của tuần này là bao nhiêu? | ① No-Grounding | Không bịa dữ liệu điểm/XP; chuyển @TA | G10/PAIR Handoff |
| Link tài liệu Lab03 đâu? | ①/② Thiếu căn cứ hoặc thiếu tài liệu | Không tự tạo link; hỏi lại hoặc chuyển @TA | G10 |
| Thông báo mới nhất là gì? | ② Low-Confidence | Hỏi rõ người dùng muốn deadline, lịch hay tài liệu | G10 |
| Tạo poll giúp tôi | ③ Out-of-Scope | Từ chối thao tác thay người dùng, hướng dẫn Poll Discord | G1 |
| Điểm danh standup có bắt buộc không? | ④ Domain Policy | Trả lời quy định và kèm nguồn | G11 |

**Kịch bản đáng sợ nhất khi demo:** TC_09 — học viên hỏi có được lùi deadline Project không. Đây là rủi ro cao nhất vì câu trả lời bịa có thể khiến học viên nộp muộn và mất điểm; bot bắt buộc phải không suy đoán và chuyển @TA.

---

## §6. Bốn đường đi của trải nghiệm

```
┌─────────────────────────────────────────────────────────────────────┐
│                        USER JOURNEY FLOW                              │
└─────────────────────────────────────────────────────────────────────┘

[User gõ câu hỏi vào Discord]
           │
           ▼
    ┌──────────────┐
    │  Bot nhận    │ ◄─── mention @Trợ lý
    │  câu hỏi    │
    └──────┬───────┘
           │
           ▼
    ┌──────────────────────────────┐
    │ AI: Tìm căn cứ trong tài    │
    │ liệu thông báo chính thức    │
    └──────────────┬───────────────┘
                   │
           ┌───────┴───────┐
           │               │
           ▼               ▼
    ┌────────────┐  ┌─────────────────┐
    │ TÌM THẤY   │  │ KHÔNG TÌM THẤY  │
    │ căn cứ     │  │ căn cứ          │
    └─────┬──────┘  └────────┬────────┘
          │                    │
          ▼                    ▼
   ┌─────────────┐    ┌──────────────────┐
   │ 1. Happy    │    │ 2. Low-confidence│
   │    Path     │    │    (②)          │
   │             │    │                  │
   │ Bot trả lời │    │ Bot hỏi làm rõ: │
   │ ngắn gọn   │    │ "Bạn đang hỏi  │
   │ + trích    │    │ về Lab hay      │
   │ dẫn nguồn │    │ Project?"       │
   │ + link     │    └────────┬─────────┘
   └─────────────┘             │
          │                    ▼
          │           ┌──────────────────┐
          │           │ User trả lời     │
          │           │ làm rõ          │
          │           └────────┬─────────┘
          │                    │
          │           ┌───────┴───────┐
          │           │               │
          │           ▼               ▼
          │    ┌───────────┐   ┌────────────────┐
          │    │ Đủ căn   │   │ Vẫn không đủ  │
          │    │ cứứ      │   │ căn cứ        │
          │    └─────┬─────┘   └───────┬────────┘
          │          │                  │
          │          ▼                  ▼
          │   [Happy Path]    ┌────────────────┐
          │                   │ 3. No-grounding │
          │                   │    (①)         │
          │                   │                 │
          │                   │ Bot: "Mình chưa │
          │                   │ tìm thấy. Tag  │
          │                   │ @TA nhé!"      │
          │                   └────────────────┘
          │                          │
          └──────────────────────────┘
                  │              │
                  ▼              ▼
         ┌─────────────────────────────┐
         │      4. CORRECTION           │
         │                              │
         │ [Nút "Sửa kết quả"]        │
         │ → User nhập lại câu hỏi     │
         │ → Hoặc [Nút "Tag TA"]       │
         │ → Chuyển trực tiếp đến TA   │
         └─────────────────────────────┘
```

### Mô tả chi tiết 4 đường đi:

**1. Happy Path (AI tự tin cao)**
- Trigger: Câu hỏi rõ ràng, có căn cứ trong tài liệu
- Bot: "Theo thông báo ngày 15/9, deadline Lab02 là 23:59 ngày 20/9. Link: #thong-bao"
- User có thể: đặt câu hỏi tiếp, bỏ qua, hoặc sửa

**2. Low-Confidence (②) — Mơ hồ, thiếu thông tin**
- Trigger: Câu hỏi không đủ cụ thể ("Khi nào nộp?", "Deadline nào?")
- Bot: "Mình cần làm rõ — bạn đang hỏi về deadline nộp bài nào? Lab hay Project?"
- User: trả lời → quay lại Happy Path hoặc No-Grounding

**3. No-Grounding (①) — Không tìm thấy căn cứ**
- Trigger: Câu hỏi ngoài tài liệu hoặc không có thông tin
- Bot: "Mình chưa tìm thấy thông tin này trong tài liệu thông báo. Bạn tag @TA để được hỗ trợ nhé!"
- User: có thể sửa câu hỏi hoặc tag TA trực tiếp

**4. Correction — User sửa/tranh thán**
- Trigger: User không hài lòng với câu trả lời
- User có thể: bấm "Sửa kết quả" để nhập lại câu hỏi, hoặc bấm "Tag TA" để chuyển trực tiếp

---

## §7. Kiểm thử

- **Chiều chất lượng (kiểm chứng được):**
  - **Factuality (Đúng & có căn cứ):** 100% thông tin trả lời phải trace được về tài liệu thông báo chính thức (`#thong-bao-khoa-hoc`, `#quy-che-khoa-hoc`). Tuyệt đối không bịa đặt; nếu không có dữ liệu bắt buộc chuyển TA. Đo: *Pass/Fail*.
  - **Relevance (Đúng trọng tâm):** Trả lời đúng câu hỏi, không lan man, không spam menu làm loãng kênh chat. Đo: *Thang 1–5 (Đạt khi ≥ 4/5)*.
  - **Conciseness & Source Citation (Ngắn gọn & Kèm nguồn):** Độ dài ≤ 200 ký tự (hoặc ≤ 3 ý), luôn có dòng trích dẫn `📌 Nguồn: [Kênh/Tài liệu]` cho câu trả lời Happy path và Domain Policy. Đo: *Pass/Fail*.

- **Golden set (24 cases — đã hoàn thiện trong `eval/`):**
  - Chi tiết file: [`eval/golden_set.json`](eval/golden_set.json) & [`eval/golden_set.md`](eval/golden_set.md).
  - Runner: [`eval/run_eval.py`](eval/run_eval.py) · phân tích lỗi: [`eval/analysis.md`](eval/analysis.md).
  - Cơ cấu: 8 case Happy path + 3 case Lớp ① (Nguồn sự thật) + 3 case Lớp ② (Mơ hồ/Hỏi lại) + 3 case Lớp ③ (Ngoài phạm vi) + 3 case Lớp ④ (Đặc thù quy chế) + 4 Edge cases (Teencode, viết tắt, bẫy tin đồn, câu hỏi ghép).
  - Trong đó có **14/24 cases (58.3%)** được trích xuất hoặc phát triển trực tiếp từ khảo sát 14 học viên lớp 3B.

- **Quality bar (khóa cứng):**
  > *"Đạt khi tổng thể ≥ 85% qua bộ kiểm thử, 100% case Lớp ① (No-Grounding) không được hallucinate/bịa đặt thông tin mà phải fallback chuyển TA, và 100% câu trả lời có căn cứ phải kèm trích dẫn nguồn."*

- **Kết quả các lượt chạy:**

| Lượt đo | Thời điểm | Số case qua | Tỷ lệ (%) | Đạt Quality Bar? | Ghi chú |
|---------|-----------|-------------|-----------|-------------------|---------|
| Run 1 (CP2) | 17/9/2026 20:00 | 24/24 | 100.0% | ✅ Đạt | Chạy kiểm thử baseline trên 24 cases qua runner `eval/run_eval.py` |
| Run 2 (CP3) | 18/9/2026 12:36 | 24/24 | 100.0% | ✅ Đạt | AI thật; No-Grounding 100%, citation 100%; phân tích tại `eval/analysis.md` và kết quả tại `eval/run-2-results.json` |
| Run 3 (CP4) | Không chạy riêng | — | — | — | Dùng Run 2 cuối 24/24 làm bằng chứng đo hồi quy; quality bar giữ nguyên |


---

## §8. Phân công & kế hoạch

| Thành viên | Mã HV | Phân công |
|------------|-------|-----------|
| Nguyễn Minh Thắng | 2A202602706 | Product Lead, spec.md, evidence mining, chốt quality bar và changelog |
| Nguyễn Thị Vàng | 2A202602897 | Prompt engineering, Golden Set (≥20 cases), eval framework, khảo sát (`eval/survey_analysis.md`) |
| Nguyễn Minh Tuấn | 2A202602420 | Prototype Discord Bot, Gemini API/fallback, logging, UI demo và video demo/pitch |

**Willing users (≥3) và kế hoạch validation CP5:**

| Người dùng | Task dùng thử | Bằng chứng cần ghi |
|---|---|---|
| Bùi Việt Anh | Tìm deadline Lab 02 và kiểm tra nguồn | Thời gian tìm, có hiểu nguồn không, quote nguyên văn |
| Hà Anh Tuấn | Hỏi một câu mơ hồ và chọn đường làm rõ | Có biết phải chọn Lab/Project không, quote nguyên văn |
| Trần Mạnh Hùng | Hỏi một case không có căn cứ và một case ngoài phạm vi | Có nhận ra fallback/@TA và giới hạn bot không, quote nguyên văn |

Validation CP5 sẽ bổ sung tối thiểu 5 người dùng ngoài nhóm, giao task rồi quan sát không hướng dẫn; lưu nhật ký, quote nguyên văn, điểm kẹt và ít nhất một thay đổi vào Changelog.

---

## §9. Changelog

| Thời điểm | Đổi gì | Vì sao |
|-----------|--------|--------|
| 17/9/2026 | Tạo spec.md đầu tiên | CP1 Canvas hoàn tất |
| 18/9/2026 | Hoàn thiện §1-§8: Evidence, Impact, Thiết kế, 4 lớp lỗi, 4 đường đi, Golden set 24 cases, Quality bar | CP4 - Hoàn thiện spec |
| 18/9/2026 | Quality bar: ≥85% tổng thể, 100% no-grounding không bịa, 100% trích dẫn nguồn | CP4 - Freeze quality bar |
| 18/9/2026 | Hoàn tất runner, sửa prompt/grounding, chạy lại Run 2 đạt 24/24 (100%), No-Grounding 100%, citation 100% | CP3/CP4 - Chốt số liệu và quality bar |
| 18/9/2026 | Bổ sung template Domain Policy, liên kết báo cáo khảo sát n=14 (`eval/survey_analysis.md`), nghiệm thu 5/5 cases prompt | CP4 - Nguyễn Thị Vàng hoàn thiện toàn diện Prompt & Eval tasks |
| 18/9/2026 | Bổ sung Evidence A/B với 5 quote nguyên văn, ma trận 10 kịch bản nghiệm thu, kịch bản rủi ro cao nhất và kế hoạch validation willing users | CP4 - Hoàn thiện spec theo rubric |
