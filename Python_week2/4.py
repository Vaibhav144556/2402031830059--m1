# marksheet 
java = int(input("Enter marks of java:"))
english = int(input("Enter marks of english:"))
maths = int(input("Enter marks of maths:"))
php = int(input("Enter marks of php:"))
python = int(input("Enter marks of python:"))
ruby = int(input("Enter marks of ruby:"))

total = java + english + maths + php + python + ruby
print("total marks=",total)

per = total / 6
print("Percentage:",per)

if per>90:
	print("A Grade")
elif (per>70) and (per<=90):
	print("B Grade")
elif (per>40) and (per<=70):
	print("C Grade")
else:
	print("D Grade")