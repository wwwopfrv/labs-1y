day = int(input("введите сегодняшнюю дату: "))
month = int(input("введите сегодняшний месяц: "))
year = int(input("введите сегодняшний год: "))

if day < 1 or day > 31:
    print ("error")
elif day > 28 and month == 2:
    print("error")
elif day == 31:
    print("1")
elif month == 12:
    print("1")
elif year == 9999:
    print ("0001")
elif year > 9999:
    print ("error")
elif month > 12:
    print ("error")
else:
    print (f"{day + 1}, {month + 1}, {year + 1}")