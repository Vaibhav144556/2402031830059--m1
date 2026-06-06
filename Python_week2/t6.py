age = int(input("Enter your age: "))
voter_id = input("Do you have a voter ID? (yes/no): ")
if age >= 18:
    if voter_id == "yes":
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")
else:
    print("You are not eligible to vote.")