reverse=""
string=input("Enter a string : ")
index=len(string)-1
while index>=0:
	reverse=reverse+string[index]
	index=index-1
print("reverse string :",reverse)