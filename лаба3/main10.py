num = int(input("введите значение от 1 до 10: "))

if num < 1 or num > 10:
    print("error")
else:
    
    result = ""

    match num:
        case 1:
            result += "bad"
        case 2:
            result += "bad"
        case 3:
            result += "bad"
        case 4:
            result += "bad"
        case 5:
            result += "normal"
        case 6:
            result += "normal"
        case 7:
            result += "good"
        case 8:
            result += "good"
        case 9:
            result += "excellent"
        case 10:
            result += "excellent"
            
print (f"{result}")