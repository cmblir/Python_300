# 71
my_variable = ()
print(type(my_variable))
# 72
movie_rank = ('닥터 스트레인지', '스플릿', '럭키')
print(movie_rank)
# 73
number_1 = (1)
print(type(number_1), number_1)
number_1 = (1, )
print(type(number_1), number_1)
# 74
t = (1, 2, 3)
t = list(t)
t[0] = 'a'
print(t)
# 75
t = 1, 2, 3, 4
print(type(t))
# 76
t = ('a', 'b', 'c')
t = list(t)
t[0] = 'A'
t = tuple(t)
print(t)
# 77
interest = ('삼성전자', 'LG전자', 'SK Hynix')
print(list(interest))
# 78
interest = ['삼성전자', 'LG전자', 'SK Hynix']
print(tuple(interest))
# 79
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)
# 80
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