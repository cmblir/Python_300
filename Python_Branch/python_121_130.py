# 121
# 사용자로부터 문자 한 개를 입력 받고, 소문자일 경우 대문자로, 대문자 일 경우, 소문자로 변경해서 출력하라.
'''
eng = input()
if str(eng).islower() == True:
    print(str(eng).upper())
else:
    print(str(eng).lower())
'''
# 122
# 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다. 사용자로부터 score를 입력받아 학점을 출력하라.
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
# 사용자로부터 달러, 엔, 유로, 또는 위안 금액을 입력받은 후 이를 원으로 변환하는 프로그램을 작성하라. 각 통화별 환율은 다음과 같다. 사용자는 100 달러, 1000 엔, 13 유로, 100 위안과 같이 금액과 통화명 사이에 공백을 넣어 입력한다고 가정한다.
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
# 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.
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
# 휴대폰 번호 앞자리에 따라 통신사는 아래와 같이 구분된다. 사용자로부터 휴대전화 번호를 입력 받고, 통신사를 출력하는 프로그램을 작성하라.
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
# 우편번호는 5자리로 구성되는데, 앞의 세자리는 구를 나타낸다. 예를들어, 강북구의 경우 010, 011, 012 세 자리로 시작한다.
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
# 주민등록번호 뒷 자리 7자리 중 첫째 자리는 성별을 나타내는데, 1, 3은 남자 2, 4는 여자를 의미한다. 사용자로부터 13자리의 주민등록번호를 입력 받은 후 성별 (남자, 여자)를 출력하는 프로그램을 작성하라.
'''
SSN = input("주민등록번호: ")
if int(SSN.split("-")[1][0]) == 1 or int(SSN.split("-")[1][0]) == 3:
    print("남자")
else:
    print("여자")
'''
# 128
# 주민등록번호의 뒷 자리 7자리 중 두번째와 세번째는 지역코드를 의미한다. 주민 등록 번호를 입력 받은 후 출생지가 서울인지 아닌지 판단하는 코드를 작성하라
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
# 주민등록번호는 13자리로 구성되는데 마지막 자리수는 주민등록번호의 유효성을 체크하는데 사용된다. 먼저 앞에서부터 12자리의 숫자에 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5를 차례로 곱한 뒤 그 값을 전부 더한다. 연산 결과 값을 11로 나누면 나머지가 나오는데 11에서 나머지를 뺀 값이 주민등록번호의 마지막 번호가 된다.
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
# 아래 코드는 비트코인의 가격 정보를 딕셔너리로 가져오는 코드이다.
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
if (float(btc['max_price']) - float(btc['min_price'])) + float(btc['opening_price']) > float(btc['max_price']):
    print('상승장')
else:
    print('하락장')