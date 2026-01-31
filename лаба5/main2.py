# num = int(input("enter ur num(0 for break): "))
count = 0
while True:
    num = int(input("enter ur num (0 for break): "))
    
    if num == 0:
        break
    # while (num := int(input("enter ur num (0 for break): "))) != 0:
    # print(f"ur num is {num}")

    if 10 <= num <= 99 and (num // 10) == (num % 10):
        count += 1
        
print(count) 

