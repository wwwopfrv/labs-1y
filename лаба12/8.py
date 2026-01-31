n = int(input("n = "))

students = []
for i in range(n):
    surname = input("Фамилия: ")
    date = input("Дата рождения: ")
    students.append([surname, date])

# students.sort(key=lambda x: x[1])

def get_key(student):
    return student[1]

students.sort(key=get_key) 

print("\nПо дате рождения:")
for s in students:
    print(f"{s[0]} - {s[1]}")

start = input("\nБуква от: ")
end = input("Буква до: ")

print(f"\nФамилии от {start} до {end}:")
for s in students:
    if s[0] and start <= s[0][0].upper() <= end:
        print(s[0])
        
