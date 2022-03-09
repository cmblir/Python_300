# 111
'''
hello = input()
print(hello * 2)
'''
# 112
'''
num = input()
print(int(num) + 10)
'''
# 113
'''
num = input()
int_num = int(num)
if int_num % 2 == 1:
    print('홀수')
else:
    print('짝수')
'''
# 114
'''
if int_num + 20 > 255:
    print(255)
else:
    print(int_num + 20)
'''
# 115
'''
if int_num >= 0 and int_num <= 255:
    print(int_num - 20)
elif int_num < 0:
    print(0)
else:
    print(255)
'''
# 116
'''
time = input()
if time[3:] == '00':
    print('정각입니다.')
else:
    print('정각이 아닙니다.')
'''
# 117
'''
fruit = ["사과", "포도", "홍시"]
favorite = input()
if favorite in fruit:
    print('정답입니다.')
else:
    print('오답입니다.')
'''
# 118
'''
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
investing = input()
if investing in warn_investment_list:
    print('투자 경고 종목입니다.')
else:
    print('투자 경고 종목이 아닙니다.')
'''
# 119
'''
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
favorite = input()
if favorite in fruit.keys():
    print('정답입니다.')
else:
    print('오답입니다.')
'''
# 120
'''
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
favorite = input()
if favorite in fruit.values():
    print('정답입니다.')
else:
    print('오답입니다.')
'''