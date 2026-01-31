n = int(input("n = "))
m = int(input("m = "))

result = []
for i in range(n):
    row = list(map(int, input().split()))
    if 0 not in row:
        result.append(row)

print("Результат:")
for row in result:
    print(*row)
