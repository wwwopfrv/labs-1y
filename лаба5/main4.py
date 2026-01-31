count = 0

while True:
    num1 = int(input("enyer ur num(0 for break): "))
    
    if num1 == 0:
        break
    
    if 100 <= num1 <= 999:
        count += 1

print(count)
