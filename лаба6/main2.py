def nums():
    firstnum = int(input("enter ur first num: "))
    secondnum = int(input("enter ur secondnum: "))
    
    if firstnum < secondnum:
        print(f"min num: {firstnum}, max num: {secondnum}")
        
    elif firstnum == secondnum:
        print("nums are equal")
        
    else:
        print(f"min num: {secondnum}, max num: {firstnum}")
        
nums()
