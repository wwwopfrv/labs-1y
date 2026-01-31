num = int(input("enter ur number: "))

if num <= 0:
    print("error")
else:
    print((sum(range(1, num+1, 2))) - (sum(range(0, num+1, 2))))
