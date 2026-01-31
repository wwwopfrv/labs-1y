# import os
# print("Current folder:", os.getcwd())
# print("Files in folder:", os.listdir())

countries = []
with open('in.txt', 'r') as f:
    for line in f:
        parts = line.strip().split(',')
        if len(parts) == 5: 
            name, capital, continent, area, population = parts
            countries.append({
                'name': name,
                'capital': capital,
                'continent': continent,
                'area': float(area),
                'population': int(population)
            })
            
with open('in.txt', 'r') as f_in, open('Tara.dat', 'wb') as f_out: 
    f_out.write(f_in.read().encode()) 

# f_in = open('in.txt', 'r')  
# f_out = open('Tara.dat', 'wb') 

# f_out.write(f_in.read().encode())  

# f_in.close()  
# f_out.close()

search_capital = input("enter capital: ").strip()

found = None
for country in countries:
    if country['capital'].lower() == search_capital.lower():
        found = country
        break

max_area = 0
for country in countries:
    if country['area'] > max_area:
        max_area = country['area']

biggest_countries = []
for country in countries:
    if country['area'] == max_area:
        biggest_countries.append(country['name'])

sorted_countries = sorted(countries, key=lambda x: x['population'], reverse=True)
# def get_population(x):
    # return x['population'] - но через лямбду проще и короче тепа


with open('out.txt', 'w') as f: 
    f.write("1. search be capital:\n")
    if found: 
        f.write(f"country: {found['name']}, Континент: {found['continent']}\n")
    else:
        f.write(f"capiital '{search_capital}' not found\n")
    
    f.write("\n2. countries with the largest area: \n")
    for name in biggest_countries:
        f.write(f"- {name}\n")
    
    f.write("\n3. all counties b population: \n")
    for country in sorted_countries:
        f.write(f"{country['name']}: {country['population']} people\n")
        
