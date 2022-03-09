# 21
letters = 'python'
print(letters[0], letters[2])
# 22
license_plate = "24가 2210"
print(license_plate[-4:])
# 23
string = "홀짝홀짝홀짝"
print(string[::2]) # 시작인덱스:끝인덱스:오프셋
# 24
string = "PYTHON"
print(string[::-1])
# 25
phone_number = "010-1111-2222"
print(phone_number.replace("-"," "))
# 26
print(phone_number.replace("-",""))
# 27
url = "https://sharebook.kr"
print(url.split(".")[-1])
# 28
lang = 'python'
# lang[0] = 'P'
# TypeError: 'str' object does not support item assignment 라는 에러가 나온다.
print(lang)
# 29
string = 'abcdfe2a354a32a'
string_a = string.replace('a', 'A')
print(string_a)
# 30
string = 'abcd'
string.replace('b', 'B')
print(string)
print(string.replace('b', 'B'))