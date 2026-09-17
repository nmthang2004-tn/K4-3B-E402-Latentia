# Canvas CP1 — B1 · Trợ lý Discord

## Thông tin nhóm
| Họ và Tên | Mã HV | Vai trò |
|---|---|---|
| [Người 1] | HV001 | Spec + Evidence |
| [Người 2] | HV002 | Prompt + Golden Set |
| [Người 3] | HV003 | Build Prototype |

## Canvas 7 dòng

**Track:** B1 · Tối ưu Trợ lý Discord
**Job executor:** Học viên K4 đang hỏi về deadline/logistics trên Discord
**Pain:** HV hỏi "hạn nộp lab" hoặc "điểm danh" → bot trả dài nhưng không đúng thông tin cần → HV nhận deadline sai hoặc vẫn không biết

**Evidence đầu:**
- Mining 1,092 tin: 89 tin hỏi logistics (deadline, điểm danh, XP)
- Bot trả 23 lần dài (>500 ký tự) nhưng không đúng trọng tâm
- 12 câu hỏi deadline không ai trả lời

**Lát cắt 1 câu:**
> Một học viên · hỏi "hạn nộp lab 2 là khi nào" · bot chỉ trả lời khi tìm được trong thông báo chính thức, nếu không thì tag TA · học viên không nhận deadline sai.

**Automation:** Conditional — trả lời khi có căn cứ trong nguồn chính thức / chuyển TA khi không tìm được

**Willing users:**
- [Tên HV1] — sẵn sàng test
- [Tên HV2] — sẵn sàng test

**Phân công:**
- Người 1: Viết spec.md, mining data → evidence
- Người 2: Viết prompt intent classification, tạo golden set 20+ cases
- Người 3: Build prototype với ≥1 API call thật
