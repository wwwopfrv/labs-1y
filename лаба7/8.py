def treug(a, b, c):

    if  0 < a <= 10000 and 0 < b <= 10000 and 0 < c <= 10000:
        sum1 = a + b
        sum2 = a + c
        sum3 = c + b
        if sum1 > c and sum2 > b and sum3 > a:
            return True
        else:
            return False
    else:
        print('pipipupu')
        return None


while True:
    a = int(input("enter first part: "))
    b = int(input("enter second part: "))
    c = int(input("enter third part: "))
    
    if a == 0 or b == 0 or c == 0: break
    
    print(treug(a, b, c))
