num = int(input("Enter number:"))

if num%5 == 0:
	print("Div by 5")
else:
	if num%4==0:
		print("Divisble by 4")
	else:
		print("Not divisble by 5 and 4")