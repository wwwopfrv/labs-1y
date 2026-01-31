n = int(input("Сколько блюд? "))

names = []
prices = []
calories = []

for i in range(n):
    print(f"\nБлюдо {i+1}:")
    names.append(input("  Название: "))
    prices.append(float(input("  Цена: ")))
    calories.append(int(input("  Калории: ")))

min_cal = min(calories)

print("\n Блюда с минимальными калориями")
for i in range(n):
    if calories[i] == min_cal:
        print(f"{names[i]} - {calories[i]} ккал")

menu = list(zip(prices, names, calories))
menu.sort()

print("\n Блюда по возрастанию цены")
for price, name, cal in menu:
    print(f"{name}: {price:.2f} руб. ({cal} ккал)")