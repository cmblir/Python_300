# 191
import re


data = [
    [2000,  3050,  2050,  1980],
    [7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for i in data:
    for j in i:
        commision = j * (14/100000)
        print(j + commision)
# 192
for i in data:
    for j in i:
        commision = j * (14/100000)
        print(j + commision)
    print("-----")

# 193
result = []
for i in data:
    for j in i:
        commision = j * (14/100000)
        result.append(j + commision)
print(result)
# 194
result = []
for i in data:
    tmp = []
    for j in i:
        commision = j * (14/100000)
        tmp.append(j + commision)
    result.append(tmp)
print(result)
# 195
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc[1:]:
    print(i[3])
# 196
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc[1:]:
    if i[3] >= 150:
        print(i[3])
# 197
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc[1:]:
    if i[3] >= i[0]:
        print(i[3])
# 198
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
volatility = []
for i in ohlc[1:]:
    volatility.append(i[1] - i[2])
print(volatility)
# 199
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc[1:]:
    tmp = (i[3] - i[0])
    if tmp > 0:
        print(tmp)
# 200
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
tmp = 0
for i in ohlc[1:]:
    tmp += (i[3] - i[0])
print(tmp)
