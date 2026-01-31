length = int(input("Enter length: "))
n = int(input("Enter measure number: "))

if n > 5 or n < 1:
    print('Error')
else:
    match n:
        case 1:
            print(f"{length / 10} метров")
        case 2:
            print(f"{length * 1000} метров")
        case 3:
            print(f"{length} метров")
        case 4:
            print(f"{length / 1000} метров")
        case 5:
            print(f"{length / 100} метров")

