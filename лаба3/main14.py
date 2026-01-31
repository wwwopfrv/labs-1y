from math import sqrt
value = int(input("введите известное значение: "))
if value < 0:
     print("error")
     
option = int(input("""
    1 - катет (a)
    2 - гипотенуза (c)
    3 - высота проведенная к гипотенузе (h),
    4 - площадь (s)
    введите известную характеристику:"""))

if option < 0 or value > 4:
    print ("error")
else:
    
    match option:
        case 1:
            print(f"a = {value}, c = {value * sqrt(2)}, h = {value / sqrt(2)}, s = {(1/2) * (value * value)}")
        case 2:
            print(f"a = {value / sqrt(2)}, c = {value}, h = {value / 2}, s = {(1 / 4) * (value * value)}")
        case 3:
            print(f"a = {value * sqrt(2)}, c = {2 * value}, h = {value}, s = {value * value}")
        case 4:
            print(f"a = {sqrt(2 * value)}, c = {2 * sqrt(value)}, h = {sqrt(value)}, s = {value}")