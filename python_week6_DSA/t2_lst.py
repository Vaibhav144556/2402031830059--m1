lst=[45,56,3,4,23,34,67,46]
for i in lst:
	if i%2==0:
		print("Even no:",i)

		#even nubmers by append method print in list
even_lst = []
for i in lst:
	if i%2==0:	
		even_lst.append(i)
print("Even list : ",even_lst)

	#Even numbers by remove method

for i in lst.copy():

    if i % 2 != 0:
        lst.remove(i)

print(lst)
