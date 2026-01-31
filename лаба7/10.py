def verif(n):
    if 99999 < n < 1000000:
        for w in str(n)[0:3]:
            if w != '0':
                if int(w) % 2 == 0:
                    return "no"
        
        return "yes"


n = int(input("Enter N: "))

print(verif(n))
