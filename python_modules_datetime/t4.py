from datetime import date
from dateutil.parser import parse

mydate='2024-07-28'
print("str mydate : ",mydate)

ori_date=parse(mydate)
print("\noriginal type date(parse) : ",ori_date.month)
print("month: ",ori_date.month)
print("Extract month only : ",ori_date.strftime("%B"))
print("Extract year only : ",ori_date.strftime("%Y"))

# print day name 
print("Day name : ",ori_date.strftime("%A"))

