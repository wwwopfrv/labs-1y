def rectangle():
    num1 = float(input("enter first side: "))
    num2 = float(input("enter second side: "))

    if num1 <= 0 or num2 <= 0:
        print("side can/t be <= 0")
    else:
        print(f"P = {2 * (num1 + num2)}, s = {num1 * num2}")
        
rectangle()