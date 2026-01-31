num = int(input("введите трехзначное число:"))
num1 = num // 100
num2 = num % 100 // 10
num3 = num % 10
print(f"{num3, num2, num1}")

