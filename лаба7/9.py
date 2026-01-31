def REDUCE(a, b):
    sum = 0
    
    if a >= 10000000 or b >= 10000000:
        print("error")
    else:
        for w in str(a):
            if w != '0':
                if b % int(w) != 0:
                    sum += int(w)
    
    return sum


a = int(input("Enter A: "))
b = int(input("Enter B: "))

print(REDUCE(a, b))
