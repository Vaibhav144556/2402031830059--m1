from dateutil.parser import parse
from datetime import datetime

mydate = "28-06-2026"

# c_date = parse(mydate)

# print(type(c_date))

c_date = datetime.strptime(mydate,"%d-%m-%Y")
print(type(c_date))

time_12 = "03:15:24 PM"

# t_12 = datetime.strptime(time_12,"%I:%M:%S %p")
# print(type(t_12))

t_12 = parse(time_12)
print(t_12)

t_24 = t_12.strftime("%H:%M:%S")
print(t_24)