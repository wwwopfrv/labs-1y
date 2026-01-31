import math 

A = float(input("Введите коэффициент для x^2: "))
B = float(input("Введите коэффициент для x: "))
C = float(input("Введите свободный член: "))

print(f"Уравнение: {A}x^2 + {B}x + {C} = 0")

if A == 0:
    print("Это не квадратное уравнение (A = 0)")
else:
    d = B * B - 4 * A * C
    
    if d == 0:
        x = -B / (2 * A)
        print(f"Один корень: x = {x}")
    elif d > 0:
        x1 = (-B + math.sqrt(d)) / (2 * A)
        x2 = (-B - math.sqrt(d)) / (2 * A)
        print(f"Два корня: x1 = {x1}, x2 = {x2}")
    else:
        print("Действительных корней нет")