# *     1,2
# **    1,3
# ***   1,4
# ****  1,5

for i in range(1,5):
	for j in range(1,i+1):
		print(chr(96+j),end='')
	print('')
