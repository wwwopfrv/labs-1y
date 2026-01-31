while True:
    num1 = int(input("enter ur num: ")) 
    num2 = int(input("enter ur num (0 for break): "))  
    
    if num2 == 0:
        break
    
    while num2:
        num1, num2 = num2, num1 % num2
    
    if num1 == 1:
        print("vzaimno prostie")
    else:
        print('ne vzaimno prostie')

