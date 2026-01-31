abababa = int(input("enter your number(0 for break): "))

isPositive = abababa > 0
count = 0

while 1:
    x = int(input("enter your number(0 for break): "))
    
    if x == 0:
        break
    
    if x > 0 and isPositive == False:
        count += 1
        isPositive = True
    
    if x < 0 and isPositive == True:
        count += 1
        isPositive = False
        
print(count)

