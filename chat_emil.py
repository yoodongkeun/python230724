# chat_emil.py
import re

def find_email_address(text):
    # 이메일 주소를 찾기 위한 정규식 패턴
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

    # re.search()를 사용하여 텍스트에서 첫 번째 이메일 주소 찾기
    match = re.search(email_pattern, text)

    if match:
        return match.group()
    else:
        return None

# 테스트 예제 1: 텍스트 중간에 기본적인 이메일 주소가 있는 경우
input_text = "Please contact support@example.com for any inquiries."
assert find_email_address(input_text) == "support@example.com"
# 함수는 정확하게 이메일 주소 "support@example.com"를 찾아 반환해야 합니다.

# 테스트 예제 2: 텍스트 시작 부분에 이메일 주소가 있는 경우
input_text = "info@example.com is the email address you can use to reach us."
assert find_email_address(input_text) == "info@example.com"
# 함수는 정확하게 이메일 주소 "info@example.com"를 찾아 반환해야 합니다.

# 테스트 예제 3: 텍스트 끝 부분에 이메일 주소가 있는 경우
input_text = "For any assistance, you can email us at help@example.com"
assert find_email_address(input_text) == "help@example.com"
# 함수는 정확하게 이메일 주소 "help@example.com"를 찾아 반환해야 합니다.

# 테스트 예제 4: 텍스트에 여러 개의 이메일 주소가 있는 경우, 첫 번째로 발견된 것 반환
input_text = "Please contact sales@example.com or support@example.com for help."
assert find_email_address(input_text) == "sales@example.com"
# 함수는 처음으로 발견되는 이메일 주소 "sales@example.com"를 찾아 반환해야 합니다.

# 테스트 예제 5: 텍스트에 이메일 주소가 없는 경우
input_text = "Please call our support team for assistance."
assert find_email_address(input_text) == None
# 함수는 텍스트에 이메일 주소가 없으므로 None을 반환해야 합니다.

# 테스트 예제 6: 이메일 주소의 사용자 이름에 하이픈이 있는 경우
input_text = "You can reach jane-doe@example.com for further information."
assert find_email_address(input_text) == "jane-doe@example.com"
# 함수는 정확하게 이메일 주소 "jane-doe@example.com"를 찾아 반환해야 합니다.

# 테스트 예제 7: 이메일 주소의 도메인 이름에 서브도메인이 있는 경우
input_text = "Contact support@sub.example.com for technical issues."
assert find_email_address(input_text) == "support@sub.example.com"
# 함수는 정확하게 이메일 주소 "support@sub.example.com"를 찾아 반환해야 합니다.

# 테스트 예제 8: 이메일 주소의 최상위 도메인이 두 글자인 경우
input_text = "You can reach us at info@example.co.uk for any questions."
assert find_email_address(input_text) == "info@example.co.uk"
# 함수는 정확하게 이메일 주소 "info@example.co.uk"를 찾아 반환해야 합니다.

# 테스트 예제 9: 이메일 주소의 사용자 이름에 밑줄이 있는 경우
input_text = "For personalized assistance, email user_name@example.com"
assert find_email_address(input_text) == "user_name@example.com"
# 함수는 정확하게 이메일 주소 "user_name@example.com"를 찾아 반환해야 합니다.

# 테스트 예제 10: 이메일 주소의 도메인 이름에 숫자가 포함된 경우
input_text = "Contact us at support@123example.com for any issues."
assert find_email_address(input_text) == "support@123example.com"
# 함수는 정확하게 이메일 주소 "support@123example.com"를 찾아 반환해야 합니다.

