# string format -- datetime
from dateutil.parser import parse

mydate = "2026-04-26"
print(mydate)

c_date = parse(mydate)
print(c_date)
print(type(c_date))

mdy = c_date.strftime("%m-%d-%Y")
print(mdy)