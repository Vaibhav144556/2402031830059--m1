num = int(input("Enter number: "))

original = num
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + (digit ** 3)
    num = num // 10

if original == sum:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")