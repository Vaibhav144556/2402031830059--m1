from datetime import datetime

mydate='2025-5-31'
ori_date=parse(mydate)
print("date : ",ori_date)

dmy=ori_date.strftime("%d-%m-%Y")
print("\ndmy formate date  : ",dmy)