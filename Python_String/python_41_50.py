# 41
# 다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경하세요.
ticker = "btc_krw"
ticker_upper = ticker.upper()
print(ticker_upper)
# 42
#다음과 같은 문자열이 있을 때 이를 소문자 btc_krw로 변경하세요.
ticker_lower = ticker_upper.lower()
print(ticker_lower)
# 43
# 문자열 'hello'가 있을 때 이를 'Hello'로 변경해보세요.
hello = "hello"
print(hello.capitalize())
# 44
# 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx'로 끝나는지 확인해보세요.
file_name = "보고서.xlsx"
file_end_xlsx = file_name.endswith("xlsx")
print(file_end_xlsx)
# 45
# 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx' 또는 'xls'로 끝나는지 확인해보세요.
file_end_xls = file_name.endswith("xls")
print(file_end_xls)
# 46
# 파일 이름이 문자열로 저장되어 있을 때 startswith 메서드를 사용해서 파일 이름이 '2020'로 시작하는지 확인해보세요.
file_name = "2020_보고서.xlsx"
file_name_start_2020 = file_name.startswith("2020")
print(file_name_start_2020)
# 47
# 다음과 같은 문자열이 있을 때 공백을 기준으로 문자열을 나눠보세요.
a = "hello world"
a_split = a.split(" ")
print(a_split)
# 48
# 다음과 같이 문자열이 있을 때 btc와 krw로 나눠보세요.
ticker_split = ticker.split("_")
print(ticker_split)
# 49
# 다음과 같이 날짜를 표현하는 문자열이 있을 때 연도, 월, 일로 나눠보세요.
date = "2020-05-01"
date_year = date.split("-")[0]
date_month = date.split("-")[1]
date_day = date.split("-")[2]
print(f"{date_year}년 {date_month}월 {date_day}일")
# 50
# 문자열의 오른쪽에 공백이 있을 때 이를 제거해보세요.
data = "039490     "
print(data.rstrip(" "))
