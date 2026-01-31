num = int(input("Введите число от 100 до 999: "))
if num < 100 or num > 999:
    print("Ошибка: число должно быть от 100 до 999")
else:
    hundreds = num // 100
    tens = (num // 10) % 10
    units = num % 10
    
    if hundreds >= tens >= units:
        print(f"{hundreds}{tens}{units}")
    elif hundreds >= units >= tens:
        print(f"{hundreds}{units}{tens}")
    elif tens >= hundreds >= units:
        print(f"{tens}{hundreds}{units}")
    elif tens >= units >= hundreds:
        print(f"{tens}{units}{hundreds}")
    elif units >= hundreds >= tens:
        print(f"{units}{hundreds}{tens}")
    else:  # units >= tens >= hundreds
        print(f"{units}{tens}{hundreds}")