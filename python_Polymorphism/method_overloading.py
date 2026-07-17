class Addition:
	def __init__(self,name,id):
		self.name = name
		self.id = id

	def __init__(self,id,name,salary):
		self.id = id
		self.name = name
		self.salary = salary

id = int(input("Enter Id:"))
name = input("Enter Name:")
salary = float(input("Enter salary:"))

obj = Addition(id,name,salary)