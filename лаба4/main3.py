n = int(input("enter number of num:"))
if n == 0 or n < 0:
    print("error")
else:
    sum_odd = 0
    sum_non_odd = 0
    
    for i in range(n):
        num = float(input())
        if num % 2 == 0:
            sum_non_odd += num
        else:
            sum_odd += num
    
    num4 = sum_odd/sum_non_odd
    
    print (f"Сумма нечетных чисел:{sum_odd}")
    print (f"Сумма четных чисел: {sum_non_odd}")
    print (f"Отношение сумма(нечетные)/сумма(четные): {num4}")
