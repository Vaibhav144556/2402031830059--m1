class a:
	def parant(self,num1,num2):
		add=num1+num2;
		print("Addition : ",add)

class b(a):
	def child(self,n1,n2):
		sub=n1-n2;
		print("Subtraction : ",sub)


obj=b()
obj.parant(10, 20)
obj.child(20, 10)
