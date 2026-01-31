num = int(input("введите номер месяца: "))

if num > 12 or num < 0:
    print("error")
else:
    if 3 <= num <= 5:
        print("весна")
    elif 6 <= num <= 8: 
        print("лето")
    elif 9 <= num <= 11:
        print("осень")
    elif num in [12, 1, 2]:
        print("зима")

