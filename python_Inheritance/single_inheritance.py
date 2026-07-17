#single level inheritance

class A:
	def hello(self):
		print("Hello this is a parent class")

class B(A):

	def hi(self):
		print("Hi this is a child class")


obj=B()

obj.hello()
obj.hi()
