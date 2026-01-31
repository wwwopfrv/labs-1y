for w in range (3020, 3929):
    nums = w % 9
    
    if nums == 0:
        print (f"{w}", end=', ')