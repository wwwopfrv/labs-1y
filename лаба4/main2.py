n = int(input("number of num: "))
k = int(input("number of divisors: "))

for i in range(n):
    num = int(input("ur number:"))
    count = 0
    
    for d in range(1, num + 1):
        if num % d == 0:
            count += 1
    
    if count == k:
        print(num)