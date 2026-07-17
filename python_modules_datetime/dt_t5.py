from datetime import datetime 

cdatetime= '16:20:30'
c_date=datetime.strptime(cdatetime,'%H:%M:%S')
print(c_date)

time_12=c_date.strftime("%I:%M:%S %p")
print(time_12)
