n = int(input("Введите количество товаров: "))
products = []

for i in range(n):
    product = {
        'name': input("Название: "),
        'price': float(input("Цена: ")),
        'code': int(input("Код: "))
    }
    products.append(product)

for p in products:
    if p['code'] <= 200:
        p['price'] *= 1.05
    else:
        p['price'] *= 1.13

print("\nНовые цены:")
for p in products:
    print(f"{p['name']}: {p['price']:.2f}")
    

prices = [product['price'] for product in products] # список всех цен, без наименований  

max_price = max(prices)

for product in products:
    if product['price'] == max_price:
        print(f"{product['name']} costs {product['price']} and has code {product['code']}")
