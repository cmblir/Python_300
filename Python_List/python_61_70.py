# 61
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])
# 62
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])
# 63
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])
# 64
nums = [1, 2, 3, 4, 5]
print(nums[::-1])
# 65
interest = ['삼성전자', 'LG전자', 'Naver']
join_interest =  ','.join(str(e) for e in interest[0::2])
print(join_interest.replace(',',' '))
print(interest[0], interest[2])
# 66
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
join_interest =  ','.join(str(e) for e in interest)
print(join_interest.replace(',',' '))
print(" ".join(interest))
# 67
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("/".join(interest))
# 68
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("\n".join(interest))
# 69
string = "삼성전자/LG전자/Naver"
interest = string.split('/')
print(interest)
# 70
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
data2 = sorted(data)
print(data)
print(data2)