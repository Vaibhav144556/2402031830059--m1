from datetime import datetime
import time
s_time=datetime.now()
print("starting time : ",s_time)
def fact(n):
	if n==0 or n==1:
		return 1	
	else:
		return n * fact(n-1)

print(fact(100))
end_time=datetime.now()
print("Ending time : ",end_time)

execution_time=end_time- s_time
print("execution_time : ",execution_time)
# from datetime import datetime

# start = datetime.now()

# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * fact(n - 1)

# fact(100)

# end = datetime.now()

# diff = end - start

# print("Start :", start)
# print("End   :", end)
# print("Diff  :", diff)
# print("Microseconds :", diff.microseconds)
# print("Seconds :", diff.total_seconds())

