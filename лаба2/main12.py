num1 = int(input("введите первое число: "))
num2 = int(input("введите второе число: "))
num3 = int(input("введите третье число: "))
num4 = int(input("введите четвертое число: "))

if num1 > num2 and num1 > num3 and num1 > num4:
    print("первое число является максимальным")
else:
    print("первое число является минимальным")

if num2 > num1 and num2 > num3 and num2 > num4:
    print("второе число является максимальным")
else:
    print("второе число является минимальным")

if num3 > num1 and num3 > num2 and num3 > num4:
    print("третье число является максимальным")
else:
    print("третье число является минимальным")

if num4 > num1 and num4 > num2 and num4 > num3:
    print("четвертое число является максимальным")
else:
    print("четвертое число является минимальным")