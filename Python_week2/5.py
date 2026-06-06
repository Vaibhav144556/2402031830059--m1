# bonus

salary = int(input("Enter salary:"))

if salary<30000:
	bonus = salary * 0.1
	print(bonus)
elif salary>=30000 and salary<60000:
	bonus = salary * 0.2
	print(bonus)
else:
	bonus = salary * 0.25
	print(bonus)