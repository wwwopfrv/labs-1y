for w in range(100, 1000):
    if sum([w // 100, w // 10 % 10, w % 10]) % 5 == 0:
        print(w, end=', ')
