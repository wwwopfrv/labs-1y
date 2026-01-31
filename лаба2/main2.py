katet1 = int(input("катет: "))
katet2 = int(input("катет:"))
gipotenuza = int(input("гипотенуза: "))

if katet1 == katet2 and gipotenuza == katet1 and gipotenuza == katet2:
    print("треугольник равнобедренный")
elif katet2 == katet1:
    print("треугольник равносторонний")
elif katet1 < katet2 and gipotenuza < katet1 and gipotenuza < katet2 and katet1 > katet2 and gipotenuza > katet1 and gipotenuza > katet2:
    print("треугольник разносторонний")
elif katet1 == 0:
    print("сторона не может быть нулевой")
elif katet2 == 0:
    print("сторона не может быть нулевой")
elif gipotenuza == 0:
    print("сторона не может быть нулевой")