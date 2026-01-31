num1 = int(input("введите первое число: "))
num2 = int(input("введите второе число: "))
num3 = int(input("введите третье число: "))
num4 = int(input("введите четвертое число: "))

max_num = max(num1 , num2 , num3 , num4)
min_num = min (num1 , num2 , num3 , num4)

if num1 == max_num:
    print("первое число является максимальным")
elif num1 == min_num:
    print("первое число не является максимальным")
if num2 == max_num:
    print("второе число является максимальным")
elif num2 == min_num:
    print("второе число не является максимальным")
if num3 == max_num:
    print("третье число является максимальным")
elif num3 == min_num:
    print("третье число не является максимальным")
if num4 == max_num:
    print("четвертое число является максимальным")
elif num4 == min_num:
    print("четвертое число не является максимальным")