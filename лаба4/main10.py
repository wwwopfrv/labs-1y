n = int(input("entr ur num: "))

if n < 0 :
    print("error") 
else:
    num = 0
    for w in range(1,n):
        if n % w == 0:
            num += w 
    if n == num:
        print("perfect")

