import requests
import json
import time

# 디스코드 웹훅 URL을 여기에 붙여넣으세요.
# 예: "https://discord.com/api/webhooks/1234567890/abcdefghijklmnopqrstuvwxyz..."
DISCORD_WEBHOOK_URL = "YOUR_DISCORD_URL"

# 이벤트 목록을 가져오는 실제 API 엔드포인트
url = "https://www.megabox.co.kr/on/oh/ohe/Event/eventMngDiv.do"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/json;charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest"
}

data = {
    "currentPage": "1",
    "recordCountPerPage": "1000",
    "eventStatCd": "ONG",
    "eventTitle": "",
    "eventDivCd": "",
    "eventTyCd": "",
    "orderReqCd": "ONGlist"
}

def send_discord_notification(message):
    """디스코드 웹훅을 통해 메시지를 보냅니다."""
    if not DISCORD_WEBHOOK_URL or DISCORD_WEBHOOK_URL == "YOUR_DISCORD_WEBHOOK_URL_HERE":
        print("경고: 디스코드 웹훅 URL이 설정되지 않았습니다.")
        return

    payload = {
        "content": message # 디스코드에 보낼 메시지 내용
    }
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
        response.raise_for_status() 
        print("디스코드 알림 전송 성공!")
    except requests.exceptions.RequestException as e:
        print(f"디스코드 알림 전송 실패: {e}")

while True:
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status() 

        html_response_text = response.text

#이 if문 안에 영화 관련 정보 기입

        found_keywords = []
        if "아카자" in html_response_text:
            found_keywords.append("아카자")
        if "귀멸의 칼날" in html_response_text:
            found_keywords.append("귀멸의 칼날")
        if "무한성" in html_response_text:
            found_keywords.append("무한성")
        if "귀멸의칼날" in html_response_text: 
            found_keywords.append("귀멸의칼날")
        if "무한성편" in html_response_text:
            found_keywords.append("무한성편")

        if found_keywords:
            message = f"귀멸의 칼날 관련 이벤트가 발견되었습니다! https://www.megabox.co.kr/event/movie (키워드: {', '.join(found_keywords)})"
            print(message)
            send_discord_notification(message)
        else:
            print("아직 안뜸")

    except requests.exceptions.RequestException as e:
        print(f"API 요청 중 오류 발생: {e}")
    except Exception as e:
        print(f"예상치 못한 오류 발생: {e}")

    # 5초 대기 후 다음 루프 실행 (원하는 시간으로 조절)
    time.sleep(5)