class Bancking():
	b_name="Bank of India"

	def saving(self):
		print("this is saving account")
	def current(self):
		print("current account")
	def recurring(self):
		print("Recuring account")
obj=Bancking()
print("Bank name : ",obj.b_name)
obj.saving()
obj.current()
obj.recurring()
		