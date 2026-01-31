num = int(input("введите трехзначное число X:"))
numy = int(input("введите значение y: "))
num1 = num // 100
num2 = num % 100 // 10
num3 = num % 10
if 10 <= num1 + num2 + num3 <= 99:
    print("Сумма является двузначным числом")
else:
    print("hihi")
mul = num1 * num2 * num3
if 100 <= mul <= 999:
    print("произведение является трехзначны числом")
elif mul > num: 
    print("произведение больше начального числа")
else:
    print("произведение меньше начального числа")
div = (num1 + num2 + num3) % numy
if div == 0:
    print(f"{num} делится на {numy} без остатка")
else:
    print(f"{num} не делится на {numy} без остатка")