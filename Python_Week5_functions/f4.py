# factorial

def factorial(num):
	box = 1
	for i in range(1,num+1):
		box = box * i
	print(box)


num = int(input("Enter number:"))
factorial(num)