	

for i in range(1,5):
	for s in range(1,5-i):
		print(' ', end='')

	for j in range(1,i+1):

		# center position check
		if i == 3 and j == 2:
			print('a', end=' ')
		else:
			print('*', end=' ')

	print('')