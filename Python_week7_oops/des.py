class Test:
	def __init__(self):
		print("Constructor")

	def __del__(self):
		print("Destructor")

	def demo(self):
		print("DEmo")

obj = Test()
obj.demo()
