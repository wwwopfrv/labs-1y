n = int(input("enter n: "))
A = [0] * n

for w in range(n):
    A[w] = int(input())

has_odd = False
for i in range(n):
    if A[i] % 2 != 0:  
        has_odd = True
        break  

if has_odd:
    print("NOPE")
else:
    print("DA")