num = int(input("Введите число от 100 до 999: "))
if num < 100 or num > 999:
    print("Ошибка: число должно быть от 100 до 999")
else:
    hundreds = num // 100
    tens = (num // 10) % 10
    units = num % 10
    
    result = ""
    
    match hundreds:
        case 1:
            result += "сто"
        case 2:
            result += "двести"
        case 3:
            result += "триста"
        case 4:
            result += "четыреста"
        case 5:
            result += "пятьсот"
        case 6:
            result += "шестьсот"
        case 7:
            result += "семьсот"
        case 8:
            result += "восемьсот"
        case 9:
            result += "девятьсот"
    
    if tens > 0 or units > 0:
        result += " "
    
    if tens == 1:
        match units:
            case 0:
                result += "десять"
            case 1:
                result += "одиннадцать"
            case 2:
                result += "двенадцать"
            case 3:
                result += "тринадцать"
            case 4:
                result += "четырнадцать"
            case 5:
                result += "пятнадцать"
            case 6:
                result += "шестнадцать"
            case 7:
                result += "семнадцать"
            case 8:
                result += "восемнадцать"
            case 9:
                result += "девятнадцать"
    else:
        match tens:
            case 2:
                result += "двадцать"
            case 3:
                result += "тридцать"
            case 4:
                result += "сорок"
            case 5:
                result += "пятьдесят"
            case 6:
                result += "шестьдесят"
            case 7:
                result += "семьдесят"
            case 8:
                result += "восемьдесят"
            case 9:
                result += "девяносто"
        
        if units > 0 and tens > 0:
            result += " "
        
        match units:
            case 1:
                result += "один"
            case 2:
                result += "два"
            case 3:
                result += "три"
            case 4:
                result += "четыре"
            case 5:
                result += "пять"
            case 6:
                result += "шесть"
            case 7:
                result += "семь"
            case 8:
                result += "восемь"
            case 9:
                result += "девять"

    print(f"{num} - \"{result}\"")

