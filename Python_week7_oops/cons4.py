# def demo(**args):
# 	print(type(args))

# demo()

def demo(**args):
	print(args)
	for i in args.values():
		print(i)	

demo(name='meet',email='meet@gmail.com')