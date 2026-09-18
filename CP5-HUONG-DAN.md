# CP5 - Slide PDF + Video Demo Dự Phòng + Nộp Cuối

> **Deadline:** 22:30 ngày 18/9
> **⚠️ Đây là hạn nộp cuối cùng — sau mốc này không nộp thêm gì**

---

## Mục tiêu CP5

1. **Slide 6 trang xuất PDF** — theo chuẩn §5.1 `02-guide.md`, mỗi slide ≥1 con số/quote có nguồn
2. **Video demo dự phòng** — quay đúng phần định demo trên sân khấu (1 case chuẩn + 1 case khó)
3. **Validation willing users** *(bonus R6, tối đa +8 điểm)* — test thử với ≥3 người ngoài nhóm, ghi log
4. **Repo hoàn chỉnh** — đủ cấu trúc theo checklist §5.2 trước CP6
5. **Reflection** — mỗi người viết 1 file cá nhân

---

## Tóm tắt vai trò xuyên suốt

| Checkpoint | 🟡 Thắng (Product Lead) | 🟢 Vàng (Prompt/UX/Eval) | 🔵 Tuấn (Build/Demo) |
|:---:|---|---|---|
| CP2 | Flow diagram, spec §4-§6 | Prompt templates, mock data, golden set | Clickable prototype |
| CP3 | Golden set 24 cases, quality bar, runner | System prompt, prompt templates, test 5 cases | Discord bot, AI integration, logging, video |
| CP4 | Hoàn thiện spec §1-§9, khóa quality bar | Prompt test report, khảo sát n=14 | Kiểm tra codebase, chuẩn bị demo |
| **CP5** | **Slide 6 trang PDF + repo checklist** | **Validation willing users + reflection** | **Video demo dự phòng + reflection** |

---

## Phân công CP5 (SONG SONG — 3 người làm đồng thời)

### 🟡 Bước 1 — THẮNG: Slide PDF + Repo checklist

> **Deadline cho Thắng: 22:00** (để cả nhóm review trước khi nộp)

**Nhiệm vụ:**
- [ ] Soạn **Slide 6 trang** theo chuẩn §5.1, nội dung cụ thể:

| Slide | Nội dung | Thời lượng | Số liệu/Quote cần có |
|:---:|---|:---:|---|
| 1 | **User & Job** — Học viên K4 bị quá tải tin nhắn Discord | 45" | 142/306 câu hỏi logistics (46.4%), khảo sát 10/14 cần trích dẫn nguồn |
| 2 | **Vì sao chọn tính năng này** — Bảng impact 3 ứng viên rút gọn | 45" | Bảng so sánh từ spec §2 + lý do loại |
| 3 | **Giải pháp & Demo live** — Lát cắt + Conditional automation + demo 1 case chuẩn + 1 case khó | 2' | Flow diagram rút gọn, cost-of-error |
| 4 | **Kết quả đo** — Golden set 24/24 (100%) đối chiếu quality bar ≥85% | 45" | Quality bar đã chốt CP4 + 1 failure đáng kể nhất (Run 1) |
| 5 | **User thật nói gì** — Quote nguyên văn từ validation / golden set results | 45" | ≥2 quote có tên + thay đổi đã làm |
| 6 | **Nếu có thêm 1 tuần** — 2-3 việc ưu tiên + bài học lớn nhất | 30" | Feedback/failure chưa xử lý |

- [ ] Xuất **PDF** → `demo-slides.pdf` (KHÔNG nộp link online)
- [ ] Rà soát **repo checklist** theo §5.2:
  - [ ] `README.md` — có tên thành viên + phân công
  - [ ] `spec.md` — hoàn chỉnh §1-§9
  - [ ] `demo-slides.pdf` — slide 6 trang
  - [ ] `codebase/` — bot + prompts + logs
  - [ ] `eval/` — golden set + kết quả chạy
  - [ ] `validation/` — feedback log (nếu có)
  - [ ] `reflection/` — mỗi người 1 file
- [ ] Viết **reflection cá nhân** → `reflection/thang.md`

**Output:** `demo-slides.pdf`, `reflection/thang.md`, repo đủ cấu trúc

---

### 🟢 Bước 2 — VÀNG: Validation + Reflection

> **Deadline cho Vàng: 21:45** (để Thắng có quote cho Slide 5)

**Nhiệm vụ:**
- [ ] Liên hệ **≥3 willing users** đã khai từ CP1:
  - **Bùi Việt Anh** — task: Tìm deadline Lab 02 và kiểm tra nguồn
  - **Hà Anh Tuấn** — task: Hỏi một câu mơ hồ, chọn đường làm rõ
  - **Trần Mạnh Hùng** — task: Hỏi case không có căn cứ + case ngoài phạm vi
- [ ] Chạy phiên **validation 10 phút/người** theo quy trình §4.2:
  1. Comfort (~1'): "Mình đang đánh giá sản phẩm, không đánh giá bạn..."
  2. Giao task, quan sát không hướng dẫn
  3. Ghi hành vi + ngữ cảnh (không chỉ ghi lời nói)
  4. Thu quote nguyên văn
  5. Tổng kết điểm kẹt
- [ ] Ghi **feedback log** → `validation/feedback_log.md` theo format:

```markdown
# Validation Log — Nhóm Latentia

## Người 1: [Tên] — [Vai trò/Khóa]
- **Task giao:** ...
- **Thời gian hoàn thành:** ...
- **Hành vi quan sát:** ...
- **Quote nguyên văn:** "..."
- **Điểm kẹt:** ...
- **Quyết định thay đổi:** ...

## Người 2: ...
```

- [ ] Cập nhật **§9 Changelog** trong `spec.md` (thêm dòng CP5 validation)
- [ ] Gửi **≥2 quote nguyên văn** cho Thắng làm Slide 5
- [ ] Viết **reflection cá nhân** → `reflection/vang.md`

**Output:** `validation/feedback_log.md`, cập nhật `spec.md` §9, `reflection/vang.md`

---

### 🔵 Bước 3 — TUẤN: Video demo dự phòng + Reflection

> **Deadline cho Tuấn: 21:30** (để Thắng nhúng link vào slide nếu cần)

**Nhiệm vụ:**
- [ ] Chuẩn bị **demo script** — kịch bản quay chính xác:
  - **Case 1 (Happy path):** Hỏi deadline Lab 02 → bot trả lời kèm trích dẫn nguồn
  - **Case 2 (Case khó — No-grounding hoặc Low-confidence):** Hỏi câu không có căn cứ → bot fallback chuyển @TA
- [ ] **Dry run** — chạy thử 1-2 lần, bấm giờ đảm bảo ≤2 phút
- [ ] **Quay video demo dự phòng**:
  - Quay màn hình Discord với bot đang chạy thật (AI call thật, KHÔNG hardcode)
  - Hiển thị rõ: input user → bot thinking → output có trích dẫn
  - Chất lượng: rõ chữ, có tiếng giải thích nếu được
- [ ] Upload video → **YouTube/Drive (public)** hoặc lưu file `demo_backup.mp4`
- [ ] Đảm bảo **bot chạy ổn định** — sẵn sàng cho buổi pitch live ngày 19/9
- [ ] Viết **reflection cá nhân** → `reflection/tuan.md`

**Output:** Video demo (link public), `reflection/tuan.md`, bot sẵn sàng live

---

## Timeline CP5

```
18:30 ─── 3 người bắt đầu song song ───────────────────────────
  │
  │  🟡 Thắng: Soạn slide 6 trang
  │  🟢 Vàng:  Liên hệ willing users, chạy validation
  │  🔵 Tuấn:  Chuẩn bị demo script, dry run, quay video
  │
21:30 ─── 🔵 Tuấn xong video, gửi link cho Thắng ─────────────
21:45 ─── 🟢 Vàng xong validation, gửi quote cho Thắng ───────
22:00 ─── 🟡 Thắng xuất PDF, rà repo checklist ────────────────
22:15 ─── Cả nhóm review nhanh, commit & push ─────────────────
22:30 ─── ⏰ DEADLINE NỘP FORM CP5 ────────────────────────────
```

---

## Cấu trúc repo cuối cùng (Checklist §5.2)

```
K4-3B-E402-Latentia/
├── README.md              # Thành viên + phân công có tên
├── spec.md                # §1-§9 hoàn chỉnh
├── canvas.md              # Canvas 7 dòng (từ CP1)
├── demo-slides.pdf        # ⬅️ CP5: Slide 6 trang [THẮNG]
├── codebase/
│   ├── bot.py             # Discord bot handler
│   ├── ai_client.py       # AI API integration
│   ├── config.py          # Settings
│   ├── logger.py          # Logging
│   ├── prompts/
│   │   ├── system.md      # System prompt
│   │   └── templates/     # Prompt templates 5 đường đi
│   ├── logs/              # AI interaction logs
│   └── prototype/         # HTML prototype (CP2)
├── eval/
│   ├── golden_set.json    # 24 test cases
│   ├── run_eval.py        # Runner script
│   ├── results/           # Kết quả chạy CP2, CP3
│   ├── analysis.md        # Phân tích lỗi
│   └── survey_analysis.md # Khảo sát n=14
├── validation/            # ⬅️ CP5: Feedback log [VÀNG]
│   └── feedback_log.md
└── reflection/            # ⬅️ CP5: Mỗi người 1 file
    ├── thang.md           # [THẮNG]
    ├── vang.md            # [VÀNG]
    └── tuan.md            # [TUẤN]
```

---

## Chuẩn bị cho CP6 (Thuyết trình — 09:00 ngày 19/9)

> **Mỗi thành viên phải trả lời được** khi giám khảo hỏi ngẫu nhiên:

| Câu hỏi | Ai nên chuẩn bị kỹ nhất |
|---|---|
| "Augment hay automate — vì sao?" | Thắng (spec §4a) |
| "Failure nguy hiểm nhất?" | Vàng (golden set §7, validation) |
| "Phần bạn làm là gì?" | **Tất cả** — vibe-coding rule |
| "Phần này hoạt động thế nào?" | **Tất cả** — giải thích được phần có tên mình |

**Demo round:** 5' trình bày + 5' Q&A
- Thắng: Slide 1-2 + Slide 6 (~2')
- Vàng: Slide 4-5 (~1.5')
- Tuấn: Slide 3 + live demo (~1.5')
- **Thử giám khảo:** Giám khảo sẽ chạy 1 case lạ tại chỗ → Tuấn sẵn sàng bot

---

## Form CP5 — Điền khi xong

| Câu hỏi | Trả lời |
|-----------|----------|
| **Link slide PDF trên GitHub** | `https://github.com/nmthang2004-tn/K4-3B-E402-Latentia/blob/main/demo-slides.pdf` |
| **Link video demo dự phòng** | [TUẤN ĐIỀN - YouTube/Drive public] |

---

## ⚠️ Lưu ý quan trọng

1. **Song song, không tuần tự** — Khác CP2/CP3/CP4, lần này 3 người làm đồng thời
2. **Slide nộp PDF** — Không nộp link Google Slides/Canva (link hay hỏng quyền)
3. **Video CP5 ≠ Video CP3** — CP3 chứng minh sản phẩm chạy; CP5 là bản sao lưu cho buổi pitch
4. **Validation là BONUS** — Không bắt buộc, nhưng đáng làm vì tối đa +8 điểm R6
5. **Mỗi thành viên nói ≥1 phần** — Không để 1 người nói hết khi thuyết trình
6. **Git commit & push do cả nhóm** — Kiểm tra repo public trước 22:30
