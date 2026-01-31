n = int(input("enter n: "))
A = [0] * n

for w in range(n):
    A[w] = int(input(f"enter element{w+1}: "))
    
    all_different = True
    
for w in range(n):
    for j in range(w + 1, n):
        if A[w] == A[j]:
            all_different = False
            break
    if not all_different:
        break

if all_different:
    print("DA")
else:
    print("NET")
