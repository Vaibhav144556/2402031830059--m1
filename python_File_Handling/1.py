file = open('demo.txt','r')
print(file)

for i in file:
	print(i,end='')

file.close()