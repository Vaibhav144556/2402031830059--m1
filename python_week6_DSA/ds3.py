numbers = [25,63,85,96,24,10]
num = [2,4,5,6,2]

for i in numbers:
	if i%2==0:
		print(i)
		
print('------------')

box = 0
for i in num:
	box = box + i
print(box)