from datetime import datetime 

cdatetime= '30-08-2026'
c_date=datetime.strptime(cdatetime,'%d-%m-%Y')
print(c_date)

dmy=c_date.strftime("%d-%m-%Y")
print("dmy : ",dmy)