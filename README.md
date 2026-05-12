# pytest 기반 BAT 자동화 구조 샘플

![BAT 자동화 테스트](https://github.com/superluckyyoni/BAT-Portfolio/actions/workflows/bat_test.yaml/badge.svg)

## 만들게 된 이유

게임 QA로 일하면서 신규 빌드가 나올 때마다 BAT(Build Acceptance Test)를  
수작업으로 반복하는 것이 비효율적이라고 느끼게 되어 만들게 되었습니다.

특히 빌드가 자주 나오는 환경에서는 매번 동일한 체크리스트를 수동으로  
확인하는 데 많은 시간이 소요됐습니다.

또한 퀘스트 기능을 수동으로 확인하는 데 굉장히 많은 시간이 소요되어  
해당 테스트도 자동화하게 되면 QA 팀이 더 중요한 탐색적 테스트에 집중할 수 있다고 판단해 이 프로젝트를 만들었습니다.

기존에는 빌드마다 BAT 수작업 체크에 30분~1시간이 소요됐으나,  
자동화 후 명령어 하나로 테스트를 일괄 실행할 수 있는 구조로 개선했습니다.

## 프로젝트 범위

본 프로젝트는 실제 상용 게임 클라이언트와 직접 연동된 자동화 테스트가 아닌,  
BAT 자동화 파이프라인의 기본 구조를 검증하기 위해 제작한 Mock 기반 포트폴리오입니다.

주요 목적은 다음과 같습니다.

- Python/pytest 기반 테스트 실행 구조 구성
- HTML 테스트 리포트 생성
- GitHub Actions를 통한 push 시 자동 테스트 실행
- Discord Webhook을 통한 테스트 결과 알림
- 향후 실제 게임 프로젝트에 적용 가능한 BAT 자동화 구조 설계

따라서 테스트 대상 함수 일부는 실제 게임 클라이언트 기능이 아닌,  
자동화 흐름 검증을 위한 Mock 함수로 구성되어 있습니다.

## 자동화 내용
- **BAT 테스트**: 앱 실행, 메인메뉴 진입, 로그인, 씬 전환, 정상 종료
- **퀘스트 기능 테스트**: 수락, 연결, 분기, 보상 지급, 크래시 여부, 맵 이동
- **CSV 기반 데이터 검증**: 기획 데이터를 자동으로 읽어 보상 수치 및 퀘스트 체인 검증
- **디스코드 자동 알림**: 테스트 완료 시 결과를 디스코드 채널로 자동 전송
- **HTML 리포트 자동 생성**: 테스트 결과를 시각적으로 확인 가능

## 실행 결과

### 터미널 테스트 결과
![터미널 결과](screenshots/01_test_result.png)

### HTML 리포트
![HTML 리포트](screenshots/02_html_report.png)

### 디스코드 자동 알림

**테스트 전체 통과 시**

![디스코드 알림](screenshots/03_discord_alert.png)

**실패 항목 발생 시**

![디스코드 실패 알림](screenshots/04_discord_fail.png)

## 실행 방법

### 설치
```bash
pip install pytest pytest-html requests python-dotenv
```

### 환경 설정
`.env` 파일 생성 후 디스코드 웹훅 URL 입력
DISCORD_WEBHOOK_URL=your_webhook_url

### 테스트 실행
```bash
python -m pytest test_bat.py -v --html=report.html --self-contained-html
```

## 기술 스택
- Python
- pytest / pytest-html
- Discord Webhook
- CSV 데이터 파싱

## 파일 구조
```
BAT_Portfolio/
├── .github/workflows/bat_test.yaml  # CI 자동화
├── screenshots/                      # 결과물 스크린샷
├── test_bat.py                       # 19개 테스트 케이스
├── quest_data.csv                    # 퀘스트 기획 데이터
├── conftest.py                       # 디스코드 알림
└── README.md
```
