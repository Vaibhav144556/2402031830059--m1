# from datetime import datetime

from dateutil.parser import parse
# cdatetime=datetime.now()
# print("LIVE DATE AND TIME : ",cdatetime)
 
tm='12:30:25'
time=parse(tm)
print("time : ",time)


print("\n12 hour time")
time_12 = time.strftime("%I:%M:%S %p")
print(time_12)


print("\n24H time")
time_24 = time.strftime("%H:%M:%S")
print(time_24)