# 181
from operator import ilshift


apart = [['101', '102'],
         ['201', '202'],
         ['301', '301']]
for i in apart:
    print(i)
# 182
stock = [['시가', 100, 200, 300],
         ['종가', 80, 210, 330]]
for i in stock:
    print(i)
# 183
stock2 = {'시가': [100, 200, 300],
          '종가': [80, 210, 330]}
for i in stock2.values():
    print(i)
# 184
stock3 = {'10/10': [80, 110, 70, 90],
          '10/11': [210, 230, 190, 200]}
print(stock3)
# 185
apart = [[101, 102], [201, 202], [301, 302]]
for i in apart:
    for j in i:
        print(f"{j} 호")
# 186
apart = [[101, 102], [201, 202], [301, 302]]
for i in apart[::-1]:
    for j in i:
        print(f"{j} 호")
# 187
apart = [[101, 102], [201, 202], [301, 302]]
for i in apart[::-1]:
    for j in i[:-1]:
        print(f"{j} 호")
# 188
apart = [[101, 102], [201, 202], [301, 302]]
for i in apart:
    for j in i:
        print(f"{j} 호\n-----")
# 189
apart = [[101, 102], [201, 202], [301, 302]]
for i in apart:
    print(f"{i[0]} 호\n{i[1]} 호\n-----")
for i in apart:
    for j in i:
        print(f"{j} 호")
    print("----")
# 190
apart = [[101, 102], [201, 202], [301, 302]]
for i in apart:
    for j in i:
        print(f"{j} 호")
print("-----")
