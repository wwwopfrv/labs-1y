num = int(input("enter num: "))
count = 0
if num <= 0: 
    print("num can't be <= 0")
else:
    for w in range(1, num+1):
        if num % w == 0:
            count +=1
            
    if count > 2:
        print(f"число {num} - составное")
    elif count == 2:
        print(f"число {num} - простое")
    else: 
        print(f"число {num} - не составное и не простое")