import requests
import os
from dotenv import load_dotenv

load_dotenv()

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def send_discord(message):
    data = {"content": message}
    requests.post(WEBHOOK_URL, json=data)

def pytest_sessionfinish(session, exitstatus):
    passed = session.testscollected - session.testsfailed
    failed = session.testsfailed

    if failed == 0:
        msg = f"✅ BAT 결과: {passed}개 전체 통과! 이 빌드는 테스트 가능합니다."
    else:
        msg = f"❌ BAT 결과: {passed}개 통과 / {failed}개 실패! 빌드 확인 필요!"

    send_discord(msg)