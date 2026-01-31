n = int(input("enter n: "))
A = [0] * n

for w in range(n):
    A[w] = int(input())
    
for e in range(n):
    temp = str(A[e])
    if temp[0] == temp[-1]:
        hasSameDigits = True
    break

if hasSameDigits:
    print("В векторе ЕСТЬ элементы, первая цифра которых совпадает с последней")
else:
    print("В векторе НЕТ элементов, первая цифра которых совпадает с последней")
