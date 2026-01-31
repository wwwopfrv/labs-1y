def array_sum(a):
    if a == []:
        return 0
    else:
        summ = 0
        for number in a:
            summ += number 
        return summ
    
print(array_sum([3,4,-1,12,98]))