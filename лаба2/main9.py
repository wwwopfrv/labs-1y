num = int(input("введите значение x: "))
if num < -3:
    print(f"{num}^2 + 1 = {num^2 + 1}")
if -3 <= num <= 3:
    print(f"{num} - 2 = {num - 2}")
if num > 3:
    print(f"2*{num}^2 - 5* {num} + 1 = {2* num^2 - 5 * num + 1}")
else:
    print("hehe")