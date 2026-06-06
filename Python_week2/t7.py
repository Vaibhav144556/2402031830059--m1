age = int(input("Enter your age: "))
nation = input("Are you an Indian? (yes/no): ")

if age > 30:
    if nation == "yes":
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")
else:
    print("You are not eligible to vote.")