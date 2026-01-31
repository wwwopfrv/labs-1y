num = int(input("введите число от 1 дл 31"))
if num >= 1 and num <= 10:
    print("I декада")
elif num > 10 and num < 21:
    print("II декада")
elif num >= 21 and num < 31:
    print("III декада")
elif num == 31:
    print ("IV декада")
else:
    print("error")