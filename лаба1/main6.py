num1 = int(input("введите возраст Николая: "))
num2 = int(input("введите возраст Михая: "))
print(f"средний возраст двух лиц: {(num1 + num2) // 2}")
if num1 > num2:
    print(f"разница в возрасте: {num1 - num2}")
else: 
    print(f"разница в возрасте: {num2 - num1}")