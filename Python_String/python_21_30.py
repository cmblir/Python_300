# 21
# letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
letters = 'python'
print(letters[0], letters[2])
# 22
# 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
license_plate = "24가 2210"
print(license_plate[-4:])
# 23
# 아래의 문자열에서 '홀' 만 출력하세요.
string = "홀짝홀짝홀짝"
print(string[::2]) # 시작인덱스:끝인덱스:오프셋
# 24
# 문자열을 거꾸로 뒤집어 출력하세요.
string = "PYTHON"
print(string[::-1])
# 25
# >> phone_number = "010-1111-2222"
phone_number = "010-1111-2222"
print(phone_number.replace("-"," "))
# 26
# 25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.
print(phone_number.replace("-",""))
# 27
# url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
url = "https://sharebook.kr"
print(url.split(".")[-1])
# 28
# 아래 코드의 실행 결과를 예상해보세요.
lang = 'python'
# lang[0] = 'P'
# TypeError: 'str' object does not support item assignment 라는 에러가 나온다.
print(lang)
# 29
# 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
string = 'abcdfe2a354a32a'
string_a = string.replace('a', 'A')
print(string_a)
# 30
# 아래 코드의 실행 결과를 예상해보세요.
string = 'abcd'
string.replace('b', 'B')
print(string)
print(string.replace('b', 'B'))