data = int(input("введите текущую дату: "))
month = int(input("введите текущий месяц: "))
year = int(input("ввеитн текущий год: "))

if data == 31:
    print("дата: 1")
else:
    print (f"дата: {data + 1}")
if month == 12:
    print("месяц: 1")
else: 
    print(f"месяц: {month + 1}")
if year >= 9999:
    print ("0000")
else: 
    print(f"год: {year + 1}")
