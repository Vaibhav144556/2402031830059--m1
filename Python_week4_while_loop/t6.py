num = int(input("Enter number: "))

mul = 1

while num > 0:
    digit = num % 10
    mul = mul * digit
    num = num // 10

print("Multiplication =", mul)