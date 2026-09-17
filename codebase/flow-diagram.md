# Flow Diagram — Trợ lý Discord

> Sơ đồ luồng cho CP2 — thiết kế bốn đường đi của trải nghiệm

---

## Mermaid Diagram

```mermaid
flowchart TB
    START([User gõ câu hỏi]) --> BOT((Bot nhận câu hỏi))
    BOT --> SEARCH{AI: Tìm căn cứ<br/>trong tài liệu?}
    
    SEARCH -->|Có căn cứ| HAPPY[1. Happy Path<br/>Bot trả lời ngắn gọn<br/>+ trích dẫn nguồn]
    
    SEARCH -->|Không tìm thấy| CLARIFY{Câu hỏi có thể<br/>làm rõ được?}
    
    CLARIFY -->|Mơ hồ, hỏi lại được| LOWCONF[2. Low-Confidence<br/>Bot hỏi làm rõ:<br/>"Bạn đang hỏi<br/>về Lab hay Project?"]
    
    LOWCONF --> USER_REPLY[User trả lời]
    USER_REPLY --> SEARCH2{AI: Tìm căn cứ<br/>sau khi làm rõ?}
    
    SEARCH2 -->|Có căn cứ| HAPPY
    
    SEARCH2 -->|Vẫn không| NOGROUND[3. No-Grounding<br/>Bot: "Mình chưa tìm thấy.<br/>Tag @TA nhé!"]
    
    CLARIFY -->|Không thể làm rõ| NOGROUND
    
    HAPPY --> CORRECTION{User hài lòng?}
    CORRECTION -->|Không| CORR[4. Correction<br/>User bấm Sửa/Thử lại<br/>hoặc Tag TA]
    
    CORR -->|Sửa| USER_REPLY2[User nhập lại câu hỏi]
    USER_REPLY2 --> SEARCH
    
    CORR -->|Tag TA| END_TA([Chuyển đến TA])
    
    NOGROUND --> END_TA
    HAPPY --> END_OK([Kết thúc])
    
    style HAPPY fill:#90EE90,stroke:#228B22
    style LOWCONF fill:#FFFACD,stroke:#DAA520
    style NOGROUND fill:#FFB6C1,stroke:#DC143C
    style CORR fill:#E6E6FA,stroke:#9370DB
```

---

## Chi tiết từng đường đi

### 1. Happy Path (AI tự tin cao)
```
Trigger:  Câu hỏi rõ ràng, có căn cứ trong tài liệu
Input:    "Hạn nộp Lab02 là khi nào?"
Process:  AI tìm trong tài liệu → tìm thấy
Output:   "Theo thông báo ngày 15/9, deadline Lab02 là 23:59 ngày 20/9.
          Nguồn: #thong-bao-lab02"
Next:     User có thể hỏi tiếp / bỏ qua / bấm Sửa
```

### 2. Low-Confidence (②) — Mơ hồ, thiếu thông tin
```
Trigger:  Câu hỏi không đủ cụ thể
Input:    "Khi nào nộp?"
Process:  AI tìm → không đủ thông tin để trả lời
Output:   "Mình cần làm rõ — bạn đang hỏi về deadline nộp bài nào?
          Lab hay Project?"
Next:     User trả lời → quay lại tìm căn cứ
         Nếu vẫn không đủ → chuyển No-Grounding
```

### 3. No-Grounding (①) — Không tìm thấy căn cứ
```
Trigger:  Câu hỏi ngoài tài liệu hoặc không có thông tin
Input:    "Deadline project cuối kỳ có thay đổi không?"
Process:  AI tìm → không tìm thấy căn cứ
Output:   "Mình chưa tìm thấy thông tin này trong tài liệu thông báo.
          Bạn tag @TA để được hỗ trợ nhé!"
Next:     User có thể bấm Tag TA hoặc nhập lại câu hỏi
```

### 4. Correction — User sửa/tranh thán
```
Trigger:  User không hài lòng với câu trả lời
Action:   
  - Bấm "Sửa kết quả" → nhập lại câu hỏi
  - Bấm "Tag TA" → chuyển trực tiếp đến TA
Output:   
  - Sửa: Quay lại bước tìm căn cứ với câu hỏi mới
  - Tag TA: Tạo message mention @TA với câu hỏi gốc
```

---

## Các edge cases

### Lớp ③ — Ngoài phạm vi
```
Input:    "Viết code Python giùm tôi"
Output:   "Mình chỉ hỗ trợ tra cứu thông tin khoá học (deadline, lịch, 
          link tài liệu). Câu hỏi về code, bạn hỏi TA nhé!"
```

### Lớp ④ — Đặc thù domain
```
Input:    "Quy chế commit trễ như thế nào?"
Process:  AI tìm trong quy định khoá học → tìm thấy
Output:   "Theo Quy chế khoá học Mục 3.2:
          - Commit trễ < 24h: trừ 50% điểm
          - Commit trễ 24-48h: trừ 75% điểm
          - Commit trễ > 48h: không được nộp
          Nguồn: #quy-che-khoa-hoc"
```
