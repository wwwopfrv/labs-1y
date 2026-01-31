value = float(input("enter weight in kg:"))
option = int(input("""
    1 - kg
    2 - mg
    3 - g
    4 - t
    witch option u need: """))

if option < 1 or option > 4:
    print ("error")
else:
    
    match option:
        case 1:
            print (f"{value}")
        case 2:
            print (f"{value * 1000000}")
        case 3:
            print (f"{value * 1000}")
        case 4:
            print (f"{value / 1000}")