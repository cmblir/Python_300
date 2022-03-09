# 31
a = '3'
b = '4'
print(a + b)
# 32
print("Hi" * 3)
# 33
print('-' * 80)
# 34
t1 = 'python'
t2 = 'java'
t3 = f"{t1} {t2} "
print(t3 * 4)
# 35
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))
# 36
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))
# 37
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")
# 38
상장주식수 = "5,969,782,550"
상장주식수_replace = 상장주식수.replace(",","")
상장주식수_int = int(상장주식수_replace)
print(상장주식수_int, type(상장주식수_int))
# 39
분기 = "2020/03(E) (IFRS연결)"
분기_slice = 분기[:7]
print(분기_slice)
# 40
data = "   삼성전자    "
data_strip = data.strip()
print(data_strip)