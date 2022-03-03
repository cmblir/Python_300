# 71
# my_variable 이름의 비어있는 튜플을 만들라.
my_variable = ()
print(type(my_variable))
# 72
# 2016년 11월 영화 예매 순위 기준 top3는 다음과 같다. 영화 제목을 movie_rank 이름의 튜플에 저장하라. (순위 정보는 저장하지 않는다.)
movie_rank = ('닥터 스트레인지', '스플릿', '럭키')
print(movie_rank)
# 73
# 숫자 1 이 저장된 튜플을 생성하라.
number_1 = (1)
print(type(number_1), number_1)
number_1 = (1, )
print(type(number_1), number_1)
# 74
# 다음 코드를 실행해보고 오류가 발생하는 원인을 설명하라.
t = (1, 2, 3)
t = list(t)
t[0] = 'a'
print(t)
# 75
# 아래와 같이 t에는 1, 2, 3, 4 데이터가 바인딩되어 있다. t가 바인딩하는 데이터 타입은 무엇인가?
t = 1, 2, 3, 4
print(type(t))
# 76
# 변수 t에는 아래와 같은 값이 저장되어 있다. 변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정 하라.
t = ('a', 'b', 'c')
t = list(t)
t[0] = 'A'
t = tuple(t)
print(t)
# 77
# 다음 튜플을 리스트로 변환하라.
interest = ('삼성전자', 'LG전자', 'SK Hynix')
print(list(interest))
# 78
# 다음 리스트를 튜플로 변경하라.
interest = ['삼성전자', 'LG전자', 'SK Hynix']
print(tuple(interest))
# 79
# 다음 코드의 실행 결과를 예상하라.
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)
# 80
# 1 부터 99까지의 정수 중 짝수만 저장된 튜플을 생성하라.
def num_2():
    t = []
    for i in range(1, 99):
        if i % 2 == 1:
            pass
        else:
            t.append(i)
    return tuple(t)
print(num_2())
data = tuple(range(2, 100, 2))
print(data)