import math
num = int(input("enter ur num: "))

# if num <= 0:
#     print("error")

# else:
#     print(sum(math.factorial(w) for w in range(1, num + 1)))

summ = 0

for i in range(num):
    print(math.factorial(i), end=' ')
    summ += math.factorial(i)
print(summ)