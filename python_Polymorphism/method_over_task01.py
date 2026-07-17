class goto:
	def bank(self):
		print("I am go to withdrow money")

class want_to(goto):
	def bank(self):
		print("I went to deposite money")

class going_to(goto):
	def bank(self):
		print("I am going to bank robbery")

obj = [goto(),want_to(),going_to()]

for i in obj:
	i.bank()
