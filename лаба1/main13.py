from math import ceil
X = int(input("Введите размер первого файла: "))
Y = int(input("Введите размер второго файла: "))
Z = int(input("Введите размер третьего файла: "))
p = 1443.84
summ = X+Y+Z
print(f"понадобится {ceil(summ / p)} дискет")
