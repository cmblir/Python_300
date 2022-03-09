# 41
ticker = "btc_krw"
ticker_upper = ticker.upper()
print(ticker_upper)
# 42
ticker_lower = ticker_upper.lower()
print(ticker_lower)
# 43
hello = "hello"
print(hello.capitalize())
# 44
file_name = "보고서.xlsx"
file_end_xlsx = file_name.endswith("xlsx")
print(file_end_xlsx)
# 45
file_end_xls = file_name.endswith("xls")
print(file_end_xls)
# 46
file_name = "2020_보고서.xlsx"
file_name_start_2020 = file_name.startswith("2020")
print(file_name_start_2020)
# 47
a = "hello world"
a_split = a.split(" ")
print(a_split)
# 48
ticker_split = ticker.split("_")
print(ticker_split)
# 49
date = "2020-05-01"
date_year = date.split("-")[0]
date_month = date.split("-")[1]
date_day = date.split("-")[2]
print(f"{date_year}년 {date_month}월 {date_day}일")
# 50
data = "039490     "
print(data.rstrip(" "))
