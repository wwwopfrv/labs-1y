simvol = int(input("введиите символ"))

if simvol.isalpha():
    print("Буква")
elif simvol.isdigit(): 
    print("Цифра")
elif simvol in "+-*/=%":
    print("Оператор")
else:
    print("Неизвестный символ")
