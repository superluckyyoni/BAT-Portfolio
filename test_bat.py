# 모바일 게임 BAT (Build Acceptance Test) 자동화
# 실제 앱 연동 없이 테스트 구조를 잡은 버전

# -----------------------------------------------
# 테스트할 기능들을 가상으로 흉내내는 함수들
# (나중에 실제 앱 연동으로 교체할 부분)
# -----------------------------------------------

import csv

def check_app_launch():
    """앱 실행 확인"""
    return True

def check_main_menu():
    """메인메뉴 진입 확인"""
    return True

def check_login(user_id, password):
    """로그인 확인"""
    if user_id == "test_user" and password == "test_pw":
        return "lobby"
    return "fail"

def check_scene_transition():
    """씬 전환 확인 (로비 → 게임 → 결과창)"""
    return True

def check_app_close():
    """크래시 없이 종료 확인"""
    return True


# -----------------------------------------------
# 실제 BAT 테스트 케이스
# -----------------------------------------------

def test_1_앱_정상실행():
    """빌드 받았을 때 앱이 실행되는지"""
    assert check_app_launch() == True

def test_2_메인메뉴_진입():
    """메인메뉴까지 정상 진입되는지"""
    assert check_main_menu() == False

def test_3_로그인_성공():
    """정상 계정으로 로그인 성공하는지"""
    result = check_login("test_user", "test_pw")
    assert result == "lobby"

def test_4_로그인_실패처리():
    """잘못된 계정은 로그인 실패하는지"""
    result = check_login("wrong_user", "wrong_pw")
    assert result == "fail"

def test_5_씬전환_정상동작():
    """로비→게임→결과창 씬 전환이 되는지"""
    assert check_scene_transition() == True

def test_6_앱_정상종료():
    """크래시 없이 종료되는지"""
    assert check_app_close() == True


# -----------------------------------------------
# 퀘스트 기능 테스트
# -----------------------------------------------

def check_quest_accept(quest_id):
    """퀘스트 수락 확인"""
    accepted_quests = [101, 102, 103, 104, 105]
    return quest_id in accepted_quests

def check_quest_chain(quest_id):
    """퀘스트 완료 후 다음 퀘스트 연결 확인"""
    chain = {101: 102, 102: 103, 103: 104, 104: 105}
    return chain.get(quest_id) is not None

def check_quest_branch(choice):
    """분기 선택지에 따른 퀘스트 진행 확인"""
    branches = {
        "A": "퀘스트_A_라인",
        "B": "퀘스트_B_라인"
    }
    return branches.get(choice)

def check_quest_reward(quest_id):
    """퀘스트 보상이 기획서대로 지급되는지 확인"""
    rewards = {
        101: {"gold": 500, "exp": 1000},
        102: {"gold": 600, "exp": 1200},
        103: {"gold": 700, "exp": 1400},
    }
    return rewards.get(quest_id) is not None

def check_quest_crash():
    """퀘스트 진행 중 크래시 여부 확인"""
    return True

def check_map_transition(from_map, to_map):
    """맵 이동 원활한지 확인"""
    valid_transitions = [
        ("마을", "던전입구"),
        ("던전입구", "던전내부"),
        ("던전내부", "보스방"),
    ]
    return (from_map, to_map) in valid_transitions


def test_7_퀘스트_수락():
    """퀘스트가 정상적으로 수락되는지"""
    assert check_quest_accept(101) == False

def test_8_퀘스트_연결():
    """완료 후 다음 퀘스트로 이어지는지"""
    assert check_quest_chain(101) == True

def test_9_퀘스트_분기_A선택():
    """A 선택 시 A라인으로 진행되는지"""
    result = check_quest_branch("A")
    assert result == "퀘스트_A_라인"

def test_10_퀘스트_분기_B선택():
    """B 선택 시 B라인으로 진행되는지"""
    result = check_quest_branch("B")
    assert result == "퀘스트_B_라인"

def test_11_퀘스트_보상_지급():
    """기획서대로 보상이 지급되는지"""
    assert check_quest_reward(101) == True

def test_12_퀘스트_크래시_없음():
    """퀘스트 진행 중 크래시가 없는지"""
    assert check_quest_crash() == True

def test_13_맵_이동_던전입구():
    """마을 → 던전입구 이동이 되는지"""
    assert check_map_transition("마을", "던전입구") == True

def test_14_맵_이동_던전내부():
    """던전입구 → 던전내부 이동이 되는지"""
    assert check_map_transition("던전입구", "던전내부") == True

def test_15_맵_이동_보스방():
    """던전내부 → 보스방 이동이 되는지"""
    assert check_map_transition("던전내부", "보스방") == True


# -----------------------------------------------
# CSV 데이터 로드
# -----------------------------------------------

def load_quest_data():
    """quest_data.csv 읽어서 퀘스트 목록 반환"""
    quests = []
    with open("quest_data.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            quests.append(row)
    return quests


# -----------------------------------------------
# CSV 기반 퀘스트 데이터 검증 테스트
# -----------------------------------------------

def test_16_퀘스트_보상_gold_양수():
    """모든 퀘스트의 골드 보상이 0보다 큰지"""
    quests = load_quest_data()
    for q in quests:
        assert int(q["reward_gold"]) > 0, f"퀘스트 {q['quest_id']}: 골드 보상이 0 이하"

def test_17_퀘스트_보상_exp_양수():
    """모든 퀘스트의 경험치 보상이 0보다 큰지"""
    quests = load_quest_data()
    for q in quests:
        assert int(q["reward_exp"]) > 0, f"퀘스트 {q['quest_id']}: 경험치 보상이 0 이하"

def test_18_퀘스트_체인_연결확인():
    """마지막 퀘스트 제외하고 next_quest_id가 비어있지 않은지"""
    quests = load_quest_data()
    for q in quests[:-1]:  # 마지막 퀘스트는 제외
        assert q["next_quest_id"] != "", f"퀘스트 {q['quest_id']}: 다음 퀘스트 연결 없음"

def test_19_퀘스트_보상_증가곡선():
    """퀘스트 진행할수록 골드 보상이 증가하는지"""
    quests = load_quest_data()
    golds = [int(q["reward_gold"]) for q in quests]
    for i in range(len(golds) - 1):
        assert golds[i] < golds[i+1], f"퀘스트 {quests[i]['quest_id']}: 보상 증가 곡선 이상"