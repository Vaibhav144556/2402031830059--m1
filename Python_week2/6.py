num = int(input("Enter number:"))

if num%3==0:
	if num%7==0:
		print("num is divisble by 3 and 7")
	else:
		print("not divisble by 7 divible by only 3")
else:
	print("Not divisble by 3")