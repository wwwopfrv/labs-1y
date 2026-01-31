text = input("Текст: ").replace('.', '') 
n = int(input("n = "))

words = text.split()
for word in words:
    if len(word) == n:
        print(word)
