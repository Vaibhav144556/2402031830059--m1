import time

start 
= time.time()

def fact(n):
	if n==0 or n==1:
		return 1	
	else:
		return n * fact(n-1)

print(fact(100))

end = time.time()

print("Execution Process:",end-start)