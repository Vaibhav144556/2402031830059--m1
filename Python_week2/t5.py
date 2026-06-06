value = input("Enter a string value: ")
length = len(value)

if length <= 10:
    print("The length of the string value is: ", length)
else:
    print("(invalid string) The string value exceeds the maximum length of 10.")