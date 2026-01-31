text = input("Текст: ").replace('.', '')
words = text.split()

if words:
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    print(longest)