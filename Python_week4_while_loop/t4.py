total=0
while True:
    num = int(input("Enter number: "))
    if num != 0:
        total = total + num
    else:
        break

print("Addition of Total =", total)