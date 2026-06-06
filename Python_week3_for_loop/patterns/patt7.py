#    1 s=3
#   12 s=2
#  123 s=1
# 1234 s=0

for i in range(1,5):
	for s in range(1,5-i):
		print(' ',end='')
	for j in range(1,i+1):
		print(j,end='')
	print('')