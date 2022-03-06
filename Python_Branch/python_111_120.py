# 111
# 사용자로부터 입력받은 문자열을 두 번 출력하라. 아래는 사용자가 "안녕하세요"를 입력한 경우의 출력 결과이다.
'''
hello = input()
print(hello * 2)
'''
# 112
# 사용자로부터 하나의 숫자를 입력받고, 입력 받은 숫자에 10을 더해 출력하라.
'''
num = input()
print(int(num) + 10)
'''
# 113
# 사용자로부터 하나의 숫자를 입력 받고 짝수/홀수를 판별하라.
'''
num = input()
int_num = int(num)
if int_num % 2 == 1:
    print('홀수')
else:
    print('짝수')
'''
# 114
# 사용자로부터 값을 입력받은 후 해당 값에 20을 더한 값을 출력하라. 단 사용자가 입력한 값과 20을 더한 계산 값이 255를 초과하는 경우 255를 출력해야 한다.
'''
if int_num + 20 > 255:
    print(255)
else:
    print(int_num + 20)
'''
# 115
# 사용자로부터 하나의 값을 입력받은 후 해당 값에 20을 뺀 값을 출력하라. 단 출력 값의 범위는 0~255이다. 예를 들어 결괏값이 0보다 작은 값이되는 경우 0을 출력하고 255보다 큰 값이 되는 경우 255를 출력해야 한다.
'''
if int_num >= 0 and int_num <= 255:
    print(int_num - 20)
elif int_num < 0:
    print(0)
else:
    print(255)
'''
# 116
# 사용자로부터 입력 받은 시간이 정각인지 판별하라.
'''
time = input()
if time[3:] == '00':
    print('정각입니다.')
else:
    print('정각이 아닙니다.')
'''
# 117
# 사용자로 입력받은 단어가 아래 fruit 리스트에 포함되어 있는지를 확인하라. 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
'''
fruit = ["사과", "포도", "홍시"]
favorite = input()
if favorite in fruit:
    print('정답입니다.')
else:
    print('오답입니다.')
'''
# 118
# 투자 경고 종목 리스트가 있을 때 사용자로부터 종목명을 입력 받은 후 해당 종목이 투자 경고 종목이라면 '투자 경고 종목입니다'를 아니면 "투자 경고 종목이 아닙니다."를 출력하는 프로그램을 작성하라.
'''
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
investing = input()
if investing in warn_investment_list:
    print('투자 경고 종목입니다.')
else:
    print('투자 경고 종목이 아닙니다.')
'''
# 119
# 아래와 같이 fruit 딕셔너리가 정의되어 있다. 사용자가 입력한 값이 딕셔너리 키 (key) 값에 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
'''
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
favorite = input()
if favorite in fruit.keys():
    print('정답입니다.')
else:
    print('오답입니다.')
'''
# 120
# 아래와 같이 fruit 딕셔너리가 정의되어 있다. 사용자가 입력한 값이 딕셔너리 값 (value)에 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
'''
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
favorite = input()
if favorite in fruit.values():
    print('정답입니다.')
else:
    print('오답입니다.')
'''