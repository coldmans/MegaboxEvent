# 메가박스 이벤트 모니터링 🗡️

메가박스에서 이벤트(프리미어, 시사회 등)가 올라올 때마다 실시간으로 디스코드 알림을 보내주는 자동 모니터링 프로그램입니다.
# 주요 기능

실시간 모니터링: 5초마다 메가박스 이벤트 페이지를 자동으로 체크

키워드 감지:키워드 자동 탐지

디스코드 알림: 이벤트 발견 시 즉시 디스코드로 알림 전송

안정적인 API 사용: 메가박스 공식 API를 사용하여 차단 위험 최소화


# 설치 및 설정
1. 필요한 라이브러리 설치
pip install requests

3. 디스코드 웹훅 설정

디스코드에서 알림을 받고 싶은 채널에 들어가세요

채널 설정 → 연동 → 웹훅 → 새 웹훅 만들기

웹훅 URL을 복사하세요

코드에서 DISCORD_WEBHOOK_URL 변수에 웹훅 URL을 붙여넣으세요

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/당신의웹훅URL"

3. 프로그램 실행
   
python megabox_monitor.py

# 사용법
기본 실행
프로그램을 실행하면 5초마다 자동으로 메가박스 이벤트를 체크합니다.

python megabox_monitor.py

백그라운드 실행 (Linux/Mac)

터미널을 닫아도 계속 실행되도록 하려면:

nohup python megabox_monitor.py &

Windows에서 백그라운드 실행

PowerShell에서:

Start-Process python -ArgumentList "megabox_monitor.py" -WindowStyle Hidden

📊 실행 예시

아직 안뜸

아직 안뜸

귀멸의 칼날 관련 이벤트가 발견되었습니다! https://www.megabox.co.kr/event/movie (키워드: 귀멸의 칼날, 무한성편)

디스코드 알림 전송 성공!

# 설정 커스터마이징
체크 주기 변경

기본값은 5초입니다. 더 자주 또는 덜 자주 체크하고 싶다면:

pythontime.sleep(5)  # 5초를 원하는 시간으로 변경 (단위: 초)

키워드 추가/변경

새로운 키워드를 감지하고 싶다면:

if "새로운키워드" in html_response_text:
    found_keywords.append("새로운키워드")
알림 메시지 커스터마이징

알림 메시지를 변경하고 싶다면:

pythonmessage = f"귀멸의 칼날 관련 이벤트가 발견되었습니다! https://www.megabox.co.kr/event/movie (키워드: {', '.join(found_keywords)})"

# 문제 해결
1. 디스코드 알림이 오지 않아요

웹훅 URL이 올바른지 확인하세요

웹훅이 삭제되지 않았는지 확인하세요

인터넷 연결을 확인하세요

2. "경고: 디스코드 웹훅 URL이 설정되지 않았습니다" 메시지가 나와요

DISCORD_WEBHOOK_URL 변수에 실제 웹훅 URL을 설정했는지 확인하세요

3. API 요청 오류가 계속 발생해요

인터넷 연결을 확인하세요

메가박스 서버가 일시적으로 불안정할 수 있습니다. 잠시 후 다시 시도해보세요

4. 프로그램이 멈춰요

예외가 발생해도 프로그램은 계속 실행됩니다

콘솔 출력을 확인하여 오류 메시지를 확인하세요

📝 로그 저장 (선택사항)
실행 기록을 파일로 저장하고 싶다면 코드 시작 부분에 추가:

import logging

logging.basicConfig(
    filename='megabox_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

 그리고 print 대신 logging.info 사용

logging.info("귀멸의 칼날 관련 이벤트가 발견되었습니다!")

# 주의사항

과도한 요청 방지: 현재 5초 간격으로 설정되어 있습니다. 더 짧은 간격은 권장하지 않습니다.

서버 부하: 메가박스 서버에 부담을 주지 않도록 적절한 간격을 유지하세요.

개인 사용: 이 프로그램은 개인 사용 목적으로 만들어졌습니다.

🎯 실제 사용 팁

컴퓨터를 항상 켜두거나 클라우드 서버(AWS, Google Cloud 등)에서 실행

여러 키워드 설정으로 놓치는 이벤트 최소화

디스코드 채널을 따로 만들어서 알림 전용으로 사용

주기적으로 확인하여 프로그램이 정상 작동하는지 점검

📞 문의

프로그램 사용 중 문제가 생기거나 개선 사항이 있다면 언제든 문의하세요!
