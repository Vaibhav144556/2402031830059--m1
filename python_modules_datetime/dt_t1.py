from datetime import datetime

livedatetime = datetime.today()
print(f"live Datetime:{livedatetime}")

print(f"Hour: {livedatetime.hour}")
print(f"Minute: {livedatetime.minute}")
print(f"Second: {livedatetime.second}")

# ONLY DATE
ymd = livedatetime.strftime("%Y-%m-%d")
print(ymd)

# ONLY TIME
time_12 = livedatetime.strftime("%I:%M:%S %p")
print(time_12)

time_24 = livedatetime.strftime("%H:%M:%S")
print(time_24)