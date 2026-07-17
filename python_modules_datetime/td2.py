from datetime import datetime,timedelta

cdatetime = datetime.now()
time_12 = cdatetime.strftime("%I:%M:%S %p")
after_2hour = time_12 + timedelta(hours=3)
print(time_12)
print(after_2hour)

ymd = cdatetime.strftime("%Y-%m-%d")
print(ymd)
print(type(ymd))