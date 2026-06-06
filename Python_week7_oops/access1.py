class Person:
	__bank_name = "SBI" 

	def demo(self): # public
		print(f"Hello Demo Function")
		self.__hello()
		print(self.__bank_name)

	def __hello(self):  # private
		print("Hello Function")

obj = Person()
obj.demo()
