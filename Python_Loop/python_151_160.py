# 151
lst = [3, -20, -3, 44]
for i in lst:
    if i < 0:
        print(i)
# 152
lst = [3, 100, 23, 44]
for i in lst:
    if i % 3 ==0:
        print(i)
# 153
lst = [13, 21, 12, 14, 30, 18]
for i in lst:
    if i % 3 ==0 and i < 20:
        print(i)
# 154
lst_to = "I study python language !"
lst = lst_to.split(" ")
for i in lst:
    if len(i) > 3:
        print(i)
# 155
lst = ['A', 'b', 'c', 'D']
for i in lst:
    if i.isupper() == True:
        print(i)
# 156
lst = ['A', 'b', 'c', 'D']
for i in lst:
    if i.isupper() == False:
        print(i)
# 157
lst = ['dog', 'cat', 'parrot']
for i in lst:
    print(i[0].upper()+i[1:])
# 158
lst = ['hello.py', 'ex01.py', 'intro.hwp']
for i in lst:
    print(i.split(".")[0])
# 159
lst = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in lst:
    if i.split(".")[1] == 'h':
        print(i)
# 160
lst = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in lst:
    if i.split(".")[1] == 'h' or i.split(".")[1] == 'c':
        print(i)