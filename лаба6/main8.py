def dividors():
    num = int(input("enter ur num: "))
    if 10 <= num <= 30:
        count = 0
        for w in range (1, num + 1):
            dividors = num % w
            if dividors == 0:
                print(w, end=', ')
                count += 1
dividors()