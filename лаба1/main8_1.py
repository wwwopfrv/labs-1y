num1 = int(input("введите скорость движения Марины:"))
num2 = int(input("введите скорость движения Валентины:"))
a = int(input("введите расстояние между людьми: "))
sum = num1 + num2
if sum <= 0:
    print("error")
else:
    print (f"время:{a / sum}")
