s = int(input("сколько грамм на метр: "))
nr = int(input("введите количество грядок: "))
m = int(input("сколько метров одна грядка: "))
n = int(input("колтчество мешочков по 20г: "))

skokagramm = n * 20 
per = m * nr 
print(f"{per // s}")


