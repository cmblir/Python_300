# 파이썬 시작하기
# 1
# 화면에 Hello World 문자열을 출력하세요.
print('hello')
# 2
# 화면에 Mary's cosmetics을 출력하세요. (중간에 '가 있음에 주의하세요)
print("Mary's cosmetics")
# 3
# 화면에 아래 문장을 출력하세요. (중간에 "가 있음에 주의하세요.)
print('신씨가 소리질렀다. "도둑이야".')
# 4
# 화면에 "C:\Windows"를 출력하세요.
print('"C:\Windows"')
# 5
# 다음 코드를 실행해보고 \t와 \n의 역할을 설명해보세요.
print("안녕하세요.\n만나서\t\t반갑습니다.")
## \n은 줄바꿈, \t는 탭
# 6
# print 함수에 두 개의 단어를 입력한 예제입니다. 아래 코드의 출력 결과를 예상해봅시다.
print("오늘은", "일요일")
# 7
# print() 함수를 사용하여 다음과 같이 출력하세요.
print("naver;kakao;sk;samsung")
# 8
# print() 함수를 사용하여 다음과 같이 출력하세요.
print("naver/kakao/sk/samsung")
# 9
# 다음 코드를 수정하여 줄바꿈이 없이 출력하세요. (힌트: end='') print 함수는 두 번 사용합니다. 세미콜론 (;)은 한줄에 여러 개의 명령을 작성하기 위해 사용합니다.
print("first");print("second")
# 10
# 5/3의 결과를 화면에 출력하세요.
print(5/3)
# 파이썬 변수
# 11
# 삼성전자라는 변수로 50,000원을 바인딩해보세요. 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.
삼성전자 = 50000
총평가금액 = 삼성전자 * 10
print(총평가금액)
# 12
# 다음 표는 삼성전자의 일부 투자정보입니다. 변수를 사용해서 시가총액, 현재가, PER 등을 바인딩해보세요.
시가총액 = 298000000000000
현재가 = 50000
PER = 15.79
print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))
# 13
# 변수 s와 t에는 각각 문자열이 바인딩 되어있습니다.
s = "hello"
t = "python"
print(s + "!", t)
# 14
# 아래 코드의 실행 결과를 예상해보세요.
print(2 + 2 * 3)
# 15
# type() 함수는 데이터 타입을 판별합니다. 변수 a에는 128 숫자가 바인딩돼 있어 type 함수가 int (정수)형임을 알려줍니다.
a = "128"
print(type(a))
# 16
# 문자열 '720'를 정수형으로 변환해보세요.
num_str = "720"
num_int = int(num_str)
print(num_int+1, type(num_str))
# 17
# 정수 100을 문자열 '100'으로 변환해보세요.
num = 100
num_to_str = str(num)
print(num_to_str, type(num_to_str))
# 18
# 문자열 "15.79"를 실수(float) 타입으로 변환해보세요.
str_15 = "15.79"
float_str_15 = float(str_15)
print(float_str_15, type(float_str_15))
# 19
# year라는 변수가 문자열 타입의 연도를 바인딩하고 있습니다. 이를 정수로 변환한 후 최근 3년의 연도를 화면에 출력해보세요.
from datetime import datetime
year = "2020"
int_year = int(year)
print(datetime.today().year - 3)
print(datetime.today().year - 2)
print(datetime.today().year - 1)
# 20
# 에이컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다. 총 금액은 계산한 후 이를 화면에 출력해보세요. (변수사용하기)
aircon_month = 48584
aircon_total = aircon_month * 36
print(aircon_total)