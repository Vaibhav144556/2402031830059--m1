string = input("Enter any string:")
reverse = ""

length = len(string)-1

while length>=0:
	reverse = reverse + string[length]
	length = length - 1

print(reverse)

# for i in range(len(string)):
# 	print(string[i])	