def peremennii (): 
    a = float(input("enter x^2: "))
    b = float(input("enter x: "))
    c = float(input("enter num: "))
    
    d = (b * b ) - (4 * a * c)
    if d >= 0:
        
        x1 = (-b + d**0.5) / (2 * a)
        x2 = (-b - d**0.5) / (2 * a)

        print(f"x1 = (({-b}) + ({d}**0.5) / 2 * {a} = {x1})")
        print(f"x2 = (({-b}) - ({d}**0.5) / 2 * {a} = {x2})")

peremennii()
    