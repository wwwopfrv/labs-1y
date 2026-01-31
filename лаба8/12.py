n = int(input("enter n: "))

A = [0] * n


for w in range(n):
    A[w] = int(input())


A_first = A[:len(A) // 2]
A_secnd = A[len(A) // 2:]


A_first.sort()
A_secnd.sort(reverse=True)

print(f"{A_first + A_secnd}") 
