def nums():
    num1 = int(input("enter first num: "))
    num2 = int(input("entr second num: "))
    while num2 != 0 :
        num1, num2 = num2, num1 % num2
    nod = num1 
    nok = (num1 * num2) // nod
    
    print(f"nod = {nod}, nok = {nok}")
    
nums()


