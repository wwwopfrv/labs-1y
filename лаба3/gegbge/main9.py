from math import sqrt

value = float(input("""
1- радиус
2 - диаметр
3 - длина окружности
4 - площадь круга
Enter your value: """))
num = int(input("enter ur number: "))

match num:
    case 1:
        print(f"r = {value}, d = {value*2}, l = {2*3.14*value}, A = {3.14*value**2}")
    case 2:
        r = value / 2
        print(f"r = {r}, d = {value}, l = {2*3.14*r}, A = {3.14*r**2}")
    case 3:
        r = value / 2 / 3.14
        print(f"r = {r}, d = {2 * r}, l = {value}, A = {3.14*r**2}")
    case 4:
        r = sqrt(value / 3.14)
        print(f"r = {r}, d = {2 * r}, l = {2*3.14*r}, A = {value}")


