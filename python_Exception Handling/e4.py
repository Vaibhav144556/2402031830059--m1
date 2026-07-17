from math import factorial
user = int(input("Enter Number:"))
try: 
	ans = factorial(user)
	print(ans)

except NameError as e:
	print(e)
except ValueError as e:
	print(e)
except IndexError as e:
	print(e)