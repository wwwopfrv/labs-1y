num = int(input("enter ur num: "))

if num <= 0:
    print("error")
else:
    isPossible = False
    sum = 0
    for w in range(0, num):
        if w+(w+1) == num:
            print(f"{num} = {w} + {w+1}")
            isPossible = True
    if isPossible == False:
        print("Невозможнo")
        