# 121
'''
eng = input()
if str(eng).islower() == True:
    print(str(eng).upper())
else:
    print(str(eng).lower())
'''
# 122
'''
score = int(input())
if 100 >= score >= 81:
    print('A')
elif 80 >= score >= 61:
    print('B')
elif 60 >= score >= 41:
    print('C')
elif 40 >= score >= 21:
    print('D')
else:
    print('E')
'''
# 123
'''
money = input()
money_int = money.split(" ")[0]
money_str = money.split(" ")[1]
if money_str == '원':
    print(money)
elif money_str == '달러':
    print(f"{int(money_int) * 1167} 원")
elif money_str == '엔':
    print(f"{int(money_int) * 1.096} 원")
elif money_str == '유로':
    print(f"{int(money_int) * 1268} 원")
elif money_str == '위안':
    print(f"{int(money_int) * 171} 원")
'''
'''
trans = {
    '달러' : 1167,
    '엔' : 1.096,
    '유로' : 1268,
    '위안' : 171}
num, currency = money.split()
print(float(num) * trans[currency], '원')
'''
# 124
'''
num1 = input("number 1 : ")
num2 = input("number 2 : ")
num3 = input("number 3 : ")
if num1 > num2 and num3 :
    print(num1)
elif num2 > num3 and num1 :
    print(num2)
else:
    print(num3)
'''
# 125
'''
phone = input("휴대전화 번호 입력: ")
def number():
    for i in range(0,3):
        print(f'{i+1}번째 split : {phone.split("-")[i]}')
def phone_num():
    if phone.split("-")[0] == '011':
        print("SKT")
    elif phone.split("-")[0] == '016':
        print("KT")
    elif phone.split("-")[0] == '019':
        print("LGU")
    else:
        print("알수없음")
'''
'''
if phone.split(":")[1] == '011':
    print("당신은 SKT 사용자입니다.")
elif phone.split(":")[1] == '016':
    print("당신은 KT 사용자입니다.")
elif phone.split(":")[1] == '019':
    print("당신은 LGU 사용자입니다.")
else:
    print("알수없음")
'''
# 126
'''
post_num = input("우편번호: ")
class post:
    def state_num(self):
        split_post_num = post_num.split(" ")
        state = {
            1: '강북구',
            2: '도봉구',
            3: '노원구'
        }
        for i in split_post_num:
            if 0<= int(i[2]) <= 2:
                print(state[1])
            elif 3 <= int(i[2]) <= 5:
                print(state[2])
            else:
                print(state[3])
                
    def answer(self):
        if post_num[:3] in ['010', '011', '012']:
            print('강북구')
        elif post_num[:3] in ['014', '015', '016']:
            print('도봉구')
        else:
            print('노원구')
postnum = post()
print(postnum.state_num())
'''
# 127
'''
SSN = input("주민등록번호: ")
if int(SSN.split("-")[1][0]) == 1 or int(SSN.split("-")[1][0]) == 3:
    print("남자")
else:
    print("여자")
'''
# 128
'''
SSN = input("주민등록번호: ")
if SSN.split("-")[1][1:3] in ['00','01','02','03','04','05','06','07','08']:
    print('서울 입니다.')
elif SSN.split("-")[1][1:3] in ['09','10','11','12']:
    print('부산 입니다.')
else:
    print('모릅니다.')
'''
# 129
'''
num = input("주민등록번호: ")
계산1 = int(num[0]) * 2 + int(num[1]) * 3 + int(num[2]) * 4 + int(num[3]) * 5 + int(num[4]) * 6 + \
        int(num[5]) * 7 + int(num[7]) * 8 + int(num[8]) * 9 + int(num[9]) * 2 + int(num[10])* 3 + \
        int(num[11])* 4 + int(num[12]) * 5
계산2 = 11 - (계산1 % 11)
계산3 = str(계산2)

if num[-1] == 계산3[-1]:
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")
'''
# 130
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
if (float(btc['max_price']) - float(btc['min_price'])) + float(btc['opening_price']) > float(btc['max_price']):
    print('상승장')
else:
    print('하락장')