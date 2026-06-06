# Maximum numbers out of three numbers
def max(a,b,c):
	if(a>b):
		if(a>c):
			print("a : ",a)
		else:
			print("c : ",c)
	else:
		if (b>c):
			print("b : ",b)
		else:
			print("c : ",c)

			
a=int(input("Enter first number : "))
b=int(input("Enter first number : "))
c=int(input("Enter first number : "))
max(a,b,c)