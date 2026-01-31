# L = 2πr
# S = πr²

def radius():
    r = float(input("enter radius: "))
    if r <= 0:
        print("r can't be <= 0")
    else:
        print(f"l = {2 * 3.14 * r}, s = {3.14 * (r **2)}") 
radius()