num = int(input("ener ur num (<=18): "))

for w in range(10, 100):
    first_num = w // 10
    second_num = w % 10
    sum = first_num + second_num
    
    if sum == num:
        print(f"{w}", end=' ')

