   #   *
   #  * *
   # * * *
   #  * *
   #   *
for i in range(1,5):
	for s in range(1,5-i):
		print(' ',end='')
	for j in range(1,i+1):
		print('* ',end='')
	print('')
for i in range(3,0,-1):
	for s in range(1,5-i):
		print(' ',end='')
	for j in range(1,i+1):
		print('* ',end='')
	print('')
