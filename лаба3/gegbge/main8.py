option = int(input("""
1. Sum
2. Multiply
"""))
x = int(input("First number: "))
y = int(input("Second number: "))

match option:
    case 1: 
        print(f"{x} + {y} = {x + y}")
    case 2:
        print(f"{x} * {y} = {x * y}")

