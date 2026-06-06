# ***** s=0
#  **** s=1
#   *** s=2
#    ** s=3
#     * s=4

for i in range(5,0,-1):
	for s in range(1,6-i):
		print(' ',end='')
	for j in range(1,i+1):
		print('*',end='')
	print('')
