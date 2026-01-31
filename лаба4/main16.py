for w in range(100000, 1000000):
    first_part = w // 1000
    second_part = w % 1000
    
    sum1 = first_part // 100 + first_part // 10 % 10 + first_part % 10
    sum2 = second_part // 100 + second_part // 10 % 10 + second_part % 10
    if sum1 == sum2:
        print(w, end=', ')
