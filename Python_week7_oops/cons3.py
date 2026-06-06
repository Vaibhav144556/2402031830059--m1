class Addition:
	def __init__(self,*args):
		box = 0
		for i in args:
			box = box + i
		print(box)


obj = Addition(10,20,50,60)