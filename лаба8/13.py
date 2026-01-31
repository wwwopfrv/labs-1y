n = int(input("enter n: "))
A = [0] * n

for w in range(n):
    A[w] = int(input())
    
max_value = max(A)
min_value = min(A)

for e in range(n):
    if A[e] == min_value:
        A[e] = max_value
        
print(A)
