class Profile:
	__first_name = ""
	__contact    = 0


first_name = input("Enter your name:")
contact   = int(input("Enter contact:"))

p1 = Profile()
p1.__first_name = first_name
p1.__contact = contact

print(p1.__first_name)
print(p1.__contact)