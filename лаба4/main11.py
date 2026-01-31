for w in range(100, 1000):
    first_half = w // 10
    second_half = w % 10
    difference = first_half**2 - second_half**2
    if difference == w:
        print(f"{w}", end=' ')
