from dateutil.parser import parse
from datetime import timedelta

mytime = "15:30:26"
time_24 = parse(mytime)
print(time_24)

before_time = time_24 - timedelta(hours=3
	)
print(before_time)