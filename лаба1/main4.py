num = int(input("ввeдите четырехзначное ненулевое число:"))
num1 = num // 1000
num2 = num % 1000 // 100
num3 = num % 100 //10
num4 = num % 10
a = num1
b = num4
num4 = a
num1 = b
print(f"{num1, num2, num3, num4}")
c = num2
d = num3 
num2 = d 
num3 = c
print(f"{num1, num2, num3, num4}")
num2 = 0
num3 = 0
print(f"{num1, num2, num3, num4}")
