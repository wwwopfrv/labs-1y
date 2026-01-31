val = int(input("введите сумму денег: "))
if val <= 7:
    print("сумма должна быть не меньше 7")
else:
    if val % 5 % 3 != 0:
        print("число не кратно 5 и 3")
    else: 
        count5 = val // 5 >= 0
        while (val - count5 * 5) % 3 != 0: 
            count5 = count5 - 1
            count3 = (val - count5 * 5) // 3

        print(f"{count5} по 5 и {count3} по 3")
