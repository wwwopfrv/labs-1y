num1 = int(input("введите первое число: "))
num2 = int(input("введите второе число: "))
num3 = int(input("введите третье число: "))

max_num = max(num1, num2, num3)
min_num = min(num1, num2, num3)

if num1 == max_num and num2 == min_num:
    print(f"{num1 - num2}")
elif num2 == max_num and num1 == min_num:
    print(f"{num2 - num1}")
elif num3 == max_num and num2 == min_num:
    print(f"{num3 - num2}")
elif num2 == max_num and num3 == min_num:
    print(f"{num2 - num3}")
elif num1 == max_num and num3 == min_num:
    print(f"{num1 - num3}")
elif num3 == max_num and num1 == min_num:
    print(f"{num3 - num1}")
else: 
    print("hehe")