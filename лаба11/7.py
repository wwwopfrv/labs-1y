n = int(input("n = "))
m = int(input("m = "))

A = [list(map(int, input().split())) for _ in range(n)]

found = False
for i in range(n):
    for j in range(m):
        if A[i][j] == i + j:
            print(f"ДА: A[{i}][{j}] = {A[i][j]}")
            found = True

if not found:
    print("НЕТ")
    
for x in range(n):
    for y in range(m): 
        print(f"({x}, {y})")
