# 141
# 다음과 같이 판매가가 저장된 리스트가 있을 때 부가세가 포함된 가격을 for 문을 사용해서 화면에 출력하라. 단 부가세는 10원으로 가정한다.
lst = [100, 200, 300]
for i in lst:
    print(i + 10)
# 142
# for 문을 사용해서 리스트에 저장된 값을 다음과 같이 출력하라.
lst = ['김밥', '라면', '튀김']
for i in lst:
    print("오늘의 메뉴: ",i)
# 143
# 리스트에 주식 종목이름이 저장돼 있다.
lst = ['SK', 'SAMSUNG', 'LG']
for i in lst:
    print(len(i))
# 144
# 리스트에는 동물이름이 문자열로 저장돼 있다.
lst = ['dog', 'cat', 'parrot']
for i in lst:
    print(i, len(i))
# 145
# 리스트에 동물 이름 저장돼 있다.
lst = ['dog', 'cat', 'parrot']
for i in lst:
    print(i[0])
# 146
# 리스트에는 세 개의 숫자가 바인딩돼 있다.
lst = [1, 2, 3]
for i in lst:
    print(f"3 X {i}")
# 147
# 리스트에는 세 개의 숫자가 바인딩돼 있다.
lst = [1, 2, 3]
for i in lst:
    print(f"3 X {i} = {3*i}")
# 148
# 리스트에는 네 개의 문자열이 바인딩돼 있다.
lst = ['가', '나', '다', '라']
for i in lst[1:]:
    print(i)
# 149
# 리스트에는 네 개의 문자열이 바인딩돼 있다.
lst = ['가', '나', '다', '라']
for i in lst[: :2]:
    print(i)
# 150
# 리스트에는 네 개의 문자열이 바인딩돼 있다.
lst = ['가', '나', '다', '라']
for i in lst[: :-1]:
    print(i)