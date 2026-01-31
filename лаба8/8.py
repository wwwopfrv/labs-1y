n = int(input("Enter N:"))

A = [0] * n

for w in range(n):
    A[w] = float(input())

for w in range (1, n-1):
    if w % 2 == 0:
        A[w] = A[w] + A[0]
    else:
        A[w] = A[w] + A[n - 1]

print(A)
