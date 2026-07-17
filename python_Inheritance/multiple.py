class Demo:
	def __init__(self):
		print("The first constructor you have")

class Test:
	def hello(self):
		print("Hello we are selecting candidates.")

class Greet(Demo,Test):
	def greetings(self):
		print("Thank you for choose python developer")

obj = Greet()
obj.hello()
obj.greetings()