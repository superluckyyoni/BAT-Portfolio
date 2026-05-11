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

def pytest_runtest_logreport(report):
    """각 테스트 실패 시 즉시 디스코드로 알림"""
    if report.when == "call" and report.failed:
        msg = f"🔴 실패 항목: {report.nodeid}"
        send_discord(msg)