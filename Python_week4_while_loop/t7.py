num = int(input("Enter number: "))

sum = 0

while num > 0:
    digit = num % 10
    sum = sum + (digit * digit)
    num = num // 10

print("Answer =", sum)