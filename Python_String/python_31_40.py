# 31
# 아래 코드의 실행 결과를 예상해보세요.
a = '3'
b = '4'
print(a + b)
# 32
# 아래 코드의 실행 결과를 예상해보세요.
print("Hi" * 3)
# 33
# 화면에 '-'를 80개 출력하세요.
print('-' * 80)
# 34
# 변수에 다음과 같은 문자열이 바인딩되어 있습니다.
t1 = 'python'
t2 = 'java'
t3 = f"{t1} {t2} "
print(t3 * 4)
# 35
# 변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때 % formatting을 사용해서 다음과 같이 출력해보세요.
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))
# 36
# 문자열의 format( ) 메서드를 사용해서 035번 문제를 다시 풀어보세요.
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))
# 37
# 파이썬 3.6부터 지원하는 f-string을 사용해서 035번 문제를 다시 풀어보세요.
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")
# 38
# 삼성전자의 상장주식수가 다음과 같습니다. 컴마를 제거한 후 이를 정수 타입으로 변환해보세요.
상장주식수 = "5,969,782,550"
상장주식수_replace = 상장주식수.replace(",","")
상장주식수_int = int(상장주식수_replace)
print(상장주식수_int, type(상장주식수_int))
# 39
# 다음과 같은 문자열에서 '2020/03'만 출력하세요.
분기 = "2020/03(E) (IFRS연결)"
분기_slice = 분기[:7]
print(분기_slice)
# 40
# 문자열의 좌우의 공백이 있을 때 이를 제거해보세요.
data = "   삼성전자    "
data_strip = data.strip()
print(data_strip)