num = int(input("введите цифру от 0 дo 9:")) 

if num < 0 or num > 9:
    print("error")
else:
    match num:
        case 0:
            print("ноль")
        case 1:
            print("один")
        case 2:
            print("два")
        case 3:
            print("три")
        case 4:
            print("четыре")
        case 5:
            print("пять")
        case 6:
            print("шесть")
        case 7:
            print("семь")
        case 8:
            print("восемь")
        case 9:
            print("девять")

