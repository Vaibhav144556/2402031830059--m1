from dateutil.parser import parse

mydate='28-08-2004'
print("str mydate : ",mydate)

ori_date=parse(mydate)
print("\noriginal type date(parse) : ",ori_date)

print('ymd formate : ',ori_date.strftime("%Y-%m-%d"))
print('dmy formate : ',ori_date.strftime("%d-%m-%Y"))
