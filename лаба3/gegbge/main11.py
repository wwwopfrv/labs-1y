h = int(input("введите длину прямоугольника: "))
w = int(input("введите ширину прямоугольника: "))

if h < 0 or w < 0:
    print ("error")
else:
    value = int(input("""
    1 - вывести периметр
    2 - вывести площадь
    3 - вывести диагональ
    введите значение: """))
    
    if value < 1 or value > 3:
        print ("error")
    else:
        
        match value:
            case 1:
             print(f"2 * {h} + 2 * {w} = {2 * h + 2 * w}")
            case 2:
             print(f"{h} * {w} = {h * w}")
            case 3:
             print(f"({h}^2 + {w}^2) * 0.5 = {((h * h) + (w * w)) * 0.5}")