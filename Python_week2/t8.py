amount = float(input("Enter the purchase amount: "))

if amount > 2000 and amount < 5000:
    discount = amount * 0.1
    print("Discount amount: ", discount)
elif amount > 5000:
    discount = amount * 0.2
    print("Discount amount: ", discount)
else:
    print("No discount available.")
