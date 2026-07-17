from datetime import datetime



cdatetime = datetime.today()
print(f"Current Datetime:{cdatetime}")

print(f"Hour: {cdatetime.hour}")
print(f"Minute: {cdatetime.minute}")
print(f"Second: {cdatetime.second}")

# ONLY DATE
ymd = cdatetime.strftime("%Y-%m-%d")
print(ymd)

# ONLY TIME
time_12 = cdatetime.strftime("%I:%M:%S %p")
print(time_12)

time_24 = cdatetime.strftime("%H:%M:%S")
print(time_24)