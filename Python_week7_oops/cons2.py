# constructor 
class Abc:
	def __init__(self,a,b,c=None):
		print("Welcome Constructor")
		if c is None:
			ans = a + b 
			print(ans)
		else:
			ans = a + b + c
			print(ans)
		
obj = Abc(10,20)