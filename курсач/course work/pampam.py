# Известна следующая информация о странах: название, столица, континент, площадь страны, количество жителей.
# Необходимо построить бинарный файл Tara.dat с указанной структурой, загрузив информацию из текстового файла in.txt, 
# и записать в текстовый файл out.txt:

# 1.Страну и континент для столицы, введенной с клавиатуры;
# 2.Страны с наибольшей площадью;
# 3.Отсортировать информацию в порядке убывания по количеству жителей.

# Для альтернативного варианта предлагаются задачи, сформулированные в конце дидактического раздела "Тип данных Файл".

countries = [] #- список
with open('in.txt', 'r') as f:
    for line in f:
        parts = line.strip().split(',')
        if len(parts) == 5: # чек если линия списка состоит из пяти частей
            name, capital, continent, area, population = parts
            countries.append({ #тута добавляем словать в список. преобразуем данные где надо - то бишь ниже ласт две строчки
                'name': name,
                'capital': capital,
                'continent': continent,
                'area': float(area), #я думала как тут тепа чтоб и инпут для имени крох ну какой инпут ебаный рот ну я поняла уже а лана смари, вот этот тип данных, комплексный называется словарь
                'population': int(population)
            })

with open('in.txt', 'r') as f_in, open('Tara.dat', 'wb') as f_out: #тута файл становится бинарным
    f_out.write(f_in.read().encode()) #все байты записываюца в Tara.dat - то бишь f_out/ текст в байты

search_capital = input("enter capital: ").strip() #удаляет лишние пробелы внутри строки

# f_in = open('in.txt', 'r')  
# f_out = open('Tara.dat', 'wb') 

# f_out.write(f_in.read().encode())  

# f_in.close()  # не забудь закрыть
# f_out.close() 

found = None
for country in countries:
    if country['capital'].lower() == search_capital.lower():
        found = country #o, нашле то что надо. запоминаем ее
        break

max_area = 0
for country in countries:
    if country['area'] > max_area:
        max_area = country['area']

biggest_countries = []
for country in countries:
    if country['area'] == max_area:
        biggest_countries.append(country['name']) # - выбьет страны с наибольшей площадью

sorted_countries = sorted(countries, key=lambda x: x['population'], reverse=True) #True — сортировка по убыванию (от большего к меньшему)
#тепа я могу записать и ф формате 
# def get_population(x):
    # return x['population'] - но через лямбду проще и короче


with open('out.txt', 'w') as f: # w - write , f - просто переменная для работы с файлами
    f.write("1. search be capital:\n")
    if found: # ne none
        f.write(f"country: {found['name']}, Континент: {found['continent']}\n")
    else:
        f.write(f"capiital '{search_capital}' not found\n")
    
    f.write("\n2. countries with the largest area: \n")
    for name in biggest_countries:
        f.write(f"- {name}\n")
    
    f.write("\n3. all counties b population: \n")
    for country in sorted_countries:
        f.write(f"{country['name']}: {country['population']} чел.\n")





# ('r' = read) - команда для прочтения файла осле открытия
# with open('in.txt', 'r') as f: - безопасное открытие файла (автоматически закрывает)
# .strip() - удаляет лишние пробелы внутри строки
# len(parts) - это длина списка (сколько элементов в нем), тепа кол-во
# append() - добавляет элемент в конец списка

# 'wb' - режим записи бинарного файла (write binary)
# f_in.read() - читает весь файл сразу
# .encode() - преобразует текст в байты (для бинарного файла)
# f_out.write() - записывает данные в файл
# f_out/f_out - переменная для записи в файл


