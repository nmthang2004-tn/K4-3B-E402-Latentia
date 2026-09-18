"""
Evaluation Runner for Trợ lý Discord (K4-3B Latentia)
Tác giả: Nguyễn Thị Vàng (2A202602897) - Eval & Prompt Lead
Mục đích: Tự động chạy và đánh giá 24 test cases của Golden Set theo Quality Bar.
"""

import os
import json
import sys
from datetime import datetime

import argparse

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def run_evaluation(live_ai=False):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if base_dir not in sys.path:
        sys.path.insert(0, base_dir)

    golden_path = os.path.join(base_dir, 'eval', 'golden_set.json')
    mock_data_path = os.path.join(base_dir, 'codebase', 'mock-data.json')

    if not os.path.exists(golden_path):
        print(f"Error: Golden set not found at {golden_path}")
        return

    golden_data = load_json(golden_path)
    test_cases = golden_data.get('test_cases', [])
    mock_data = load_json(mock_data_path) if os.path.exists(mock_data_path) else {}
    mock_scenarios = mock_data.get('mock_scenarios', [])
    
    print("=" * 65)
    print("🚀 BẮT ĐẦU CHẠY KIỂM THỬ GOLDEN SET — TRỢ LÝ DISCORD (LATENTIA)")
    print(f"Tổng số test cases: {len(test_cases)}")
    print(f"Dữ liệu đối chiếu: codebase/mock-data.json ({len(mock_scenarios)} scenarios, {len(mock_data.get('knowledge_base', []))} docs)")
    print("=" * 65)

    passed_count = 0
    failed_count = 0
    results = []

    ai_assistant = None
    if live_ai:
        try:
            from codebase.ai_client import get_ai_assistant
            ai_assistant = get_ai_assistant()
            client_ready = (
                (ai_assistant.provider == "gemini" and ai_assistant.gemini_client is not None)
                or (ai_assistant.provider == "openai" and ai_assistant.openai_client is not None)
            )
            if not client_ready:
                print("❌ Không có AI client hoạt động. Hãy cấu hình API key và cài dependency trước khi chạy --live-ai.")
                return False
            print("⚡ CHẾ ĐỘ: ĐO LƯỜNG TRÊN MÔ HÌNH AI THẬT (RUN 2 - CP3)")
            print(f"Provider: {ai_assistant.provider} | Model: {getattr(ai_assistant, 'gemini_client', None) and 'Gemini' or 'Configured'}")
        except Exception as e:
            print(f"❌ Không thể khởi tạo AI Client: {e}. Quay về mock mode.")
            live_ai = False

    # Mock response generator based on system prompt logic & mock-data.json
    def mock_agent_response(case):
        inp = case['user_input'].lower()
        branch = case['expected_branch']
        
        # 1. First priority: Check exact or semantic scenario match from mock-data.json
        for sc in mock_scenarios:
            sc_input = sc.get('user_input', '').lower()
            if sc_input and (sc_input in inp or inp in sc_input):
                resp = sc.get('bot_response')
                if isinstance(resp, str):
                    return resp
                elif isinstance(resp, dict):
                    return resp.get('text', '')
        
        if branch == "happy_path":
            if "lab02" in inp or "lab 02" in inp or "lab2" in inp:
                if "link" in inp and "hạn" in inp:
                    return "Hạn nộp Lab 02 là 23:59 ngày 20/09/2026. Slide học tập tại https://vlearn.edu.vn/courses/k4-batch/materials. 📌 Nguồn: #thong-bao-khoa-hoc"
                elif "hình thức" in inp or "file zip" in inp:
                    return "Bài Lab 02 nộp link repo GitHub trên VLearn kèm file README báo cáo (không nén zip). 📌 Nguồn: #huong-dan-lab"
                elif "đồn" in inp or "dời hạn" in inp:
                    return "Hiện chưa có thông báo dời hạn; hạn nộp Lab 02 vẫn là 23:59 ngày 20/09/2026. 📌 Nguồn: #thong-bao-khoa-hoc"
                return "Hạn nộp Lab 02 là 23:59 Chủ Nhật ngày 20/09/2026 trên VLearn. 📌 Nguồn: #thong-bao-khoa-hoc"
            elif "milestone 1" in inp or "ms1" in inp:
                if "nhóm trưởng" in inp or "cả nhóm" in inp:
                    return "Mỗi nhóm nộp 1 bản duy nhất do nhóm trưởng đại diện nộp trên VLearn. 📌 Nguồn: #thong-bao-project"
                return "Hạn nộp Milestone 1 Project là 21:00 Thứ Ba ngày 22/09/2026. 📌 Nguồn: #thong-bao-project"
            elif "standup" in inp:
                if "bao lâu" in inp or "thời lượng" in inp:
                    return "Standup lớp 3B diễn ra tối đa 15 phút. 📌 Nguồn: #lich-trinh-lop-3b"
                elif "ốm" in inp:
                    return "Nếu bị ốm cần có xác nhận lý do y tế từ BTC để được xem xét không trừ điểm. 📌 Nguồn: #quy-che-khoa-hoc"
                return "Standup lớp 3B diễn ra lúc 08:30 sáng tại phòng E402 hoặc Voice 'Standup-Room-3B'. 📌 Nguồn: #lich-trinh-lop-3b"
            elif "slide" in inp or "tài liệu" in inp:
                return "Kho slide và tài liệu học tập tại: https://vlearn.edu.vn/courses/k4-batch/materials. 📌 Nguồn: #tai-lieu-hoc-tap"
            elif "ticket" in inp:
                return "Bạn gõ lệnh /ticket tại kênh #ho-tro-ky-thuat, TA trực sẽ hỗ trợ trong 30 phút. 📌 Nguồn: #kenh-ticket-ho-tro"
            elif "nộp muộn" in inp or "trừ điểm" in inp:
                return "Theo Mục 3.2 Quy chế: Nộp trễ <24h trừ 50% điểm, 24-48h trừ 75%, >48h 0 điểm bài nộp. 📌 Nguồn: #quy-che-khoa-hoc"
            elif "commit" in inp:
                return "Hệ thống kiểm tra commit timestamp trên GitHub theo Quy chế khoá học. 📌 Nguồn: #quy-che-khoa-hoc"
            return "Thông tin đã được ghi nhận. 📌 Nguồn: #thong-bao-khoa-hoc"

        elif branch == "low_confidence":
            if "khi nào nộp" in inp or "mấy giờ hết hạn" in inp:
                return "Bạn đang hỏi về bài nộp nào? Hiện có: 1. Lab 02 (hạn 20/09) hoặc 2. Milestone 1 Project (hạn 22/09)?"
            elif "link bài học" in inp:
                return "Bạn đang cần tìm link nào: slide bài giảng hay link nộp bài tập?"
            return "Bạn có thể làm rõ câu hỏi hơn được không?"

        elif branch == "no_grounding":
            if "điểm bài lab" in inp:
                return "Bot không thể tra cứu điểm cá nhân của bạn. Vui lòng xem trên VLearn hoặc liên hệ @TA nhé!"
            elif "thi giữa kỳ" in inp:
                return "Mình chưa tìm thấy lịch thi giữa kỳ (khóa học đánh giá qua Lab & Project). Bạn tag @TA để hỗ trợ nhé! 📌 Nguồn: #quy-che"
            return "Mình chưa có thông tin chính thức về nội dung này trong tài liệu. Bạn vui lòng liên hệ @TA để được giải đáp nhé!"

        elif branch == "out_of_scope":
            if "viết giúp" in inp or "cosine" in inp or "python" in inp:
                return "Mình chỉ hỗ trợ thông tin vận hành khoá học, không hỗ trợ viết code hay giải bài tập. Bạn trao đổi tại #thao-luan nhé!"
            elif "tạo một vote" in inp or "poll" in inp:
                return "Mình không thể tạo poll thay người dùng. Bạn vui lòng dùng tính năng Poll có sẵn của Discord nhé!"
            elif "điểm danh hộ" in inp:
                return "Bot không có thẩm quyền điểm danh thay thế. Bạn hãy báo TA hoặc Mentor nhé!"
            return "Yêu cầu nằm ngoài phạm vi hỗ trợ của Bot."

        return "Phản hồi mặc định"

    for tc in test_cases:
        if live_ai and ai_assistant:
            import time
            # Gemini free tier giới hạn 15 request/phút; 5 giây/request giữ
            # Run 2 trong giới hạn và tránh biến các case cuối thành lỗi 429.
            time.sleep(5.0)
            ai_res = ai_assistant.ask(tc['user_input'])
            actual_output = ai_res.get('text', '')
        else:
            actual_output = mock_agent_response(tc)
        
        # Check constraints and retain reasons so prompt regressions are actionable.
        normalized_output = actual_output.lower()
        missing_terms = [
            w for w in tc.get('expected_output_contains', [])
            if w.lower() not in normalized_output
        ]
        forbidden_terms = [
            w for w in tc.get('must_not_contain', [])
            if w.lower() in normalized_output
        ]
        pass_contains = not missing_terms
        fail_not_contains = bool(forbidden_terms)
        
        # Grounding check for layer 1 (No-grounding không được hallucinate/bịa đặt mà phải chuyển TA)
        is_layer_1 = tc['difficulty_layer'] == "Chỗ khó ①"
        hallucinated = is_layer_1 and ("ngày" in actual_output and "@TA" not in actual_output)

        # Every grounded answer must visibly cite its source.
        requires_citation = tc.get('expected_branch') == "happy_path"
        citation_present = "📌 nguồn:" in normalized_output or "nguồn:" in normalized_output
        citation_failed = requires_citation and not citation_present

        is_passed = pass_contains and (not fail_not_contains) and (not hallucinated) and (not citation_failed)
        
        status = "✅ PASS" if is_passed else "❌ FAIL"
        if is_passed:
            passed_count += 1
        else:
            failed_count += 1

        results.append({
            "id": tc['id'],
            "input": tc['user_input'],
            "layer": tc['difficulty_layer'],
            "expected_branch": tc.get('expected_branch'),
            "status": status,
            "actual_output": actual_output,
            "failure_reasons": {
                "missing_terms": missing_terms,
                "forbidden_terms": forbidden_terms,
                "hallucination_guard_failed": hallucinated,
                "citation_required": requires_citation,
                "citation_present": citation_present,
            } if not is_passed else {}
        })
        print(f"[{status}] {tc['id']} | Lớp: {tc['difficulty_layer'][:10]} | Input: \"{tc['user_input'][:35]}...\"")

    pass_rate = (passed_count / len(test_cases)) * 100
    print("-" * 65)
    print(f"📊 KẾT QUẢ TỔNG HỢP: {passed_count}/{len(test_cases)} Passed ({pass_rate:.1f}%)")
    
    layer_1_results = [r for r in results if r['layer'] == "Chỗ khó ①"]
    grounded_results = [r for r in results if r['expected_branch'] == "happy_path"]
    layer_1_passed = all(r['status'] == "✅ PASS" for r in layer_1_results)
    grounded_citations_passed = all(
        r['failure_reasons'].get('citation_present', True) for r in grounded_results
    )
    quality_bar_met = pass_rate >= 85.0 and layer_1_passed and grounded_citations_passed
    print(f"🛡️ Lớp ① No-Grounding: {'✅ 100%' if layer_1_passed else '❌ Chưa đạt 100%'}")
    print(f"📌 Grounded citations: {'✅ 100%' if grounded_citations_passed else '❌ Chưa đạt 100%'}")
    print(f"🎯 Đạt toàn bộ Quality Bar: {'✅ ĐẠT YÊU CẦU' if quality_bar_met else '❌ CHƯA ĐẠT'}")
    print("=" * 65)

    # Save run results
    now_str = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    os.makedirs(os.path.join(base_dir, 'eval', 'results'), exist_ok=True)
    
    report_data = {
        "timestamp": now_str,
        "run_type": "Live AI (CP3)" if live_ai else "Baseline Mock (CP2)",
        "total_cases": len(test_cases),
        "passed": passed_count,
        "failed": failed_count,
        "pass_rate": f"{pass_rate:.1f}%",
        "quality_bar_met": quality_bar_met,
        "strict_constraints": {
            "layer_1_no_grounding_100_percent": layer_1_passed,
            "grounded_citation_100_percent": grounded_citations_passed
        },
        "details": results
    }

    if live_ai:
        # CP3 target file
        cp3_report_file = os.path.join(base_dir, 'eval', 'run-2-results.json')
        with open(cp3_report_file, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, ensure_ascii=False, indent=2)
        print(f"📁 Đã lưu kết quả CP3 Run 2 tại: {cp3_report_file}")

    # Also save to eval/results/
    filename = 'eval_run_cp3.json' if live_ai else 'eval_run_cp2.json'
    report_file = os.path.join(base_dir, 'eval', 'results', filename)
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(report_data, f, ensure_ascii=False, indent=2)
    print(f"📁 Đã lưu báo cáo đánh giá tại: {report_file} (Thời điểm: {now_str})")
    return quality_bar_met

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Golden Set Eval Runner")
    parser.add_argument("--live-ai", action="store_true", help="Chạy kiểm thử trên mô hình AI thật (Run 2 - CP3)")
    args = parser.parse_args()

    succeeded = run_evaluation(live_ai=args.live_ai)
    raise SystemExit(0 if succeeded else 1)
