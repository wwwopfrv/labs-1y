a = int(input("введите рост Иона:"))
b = int(input("введите рост Андрея:"))
c = int(input("введите рост Дана:"))

if a > b and b > c:
    print("ион, андрей, дан")
else:
    print("дан, андрей, ион")
if b > a and a > c:
    print("андрей, ион, дан")
else:
    print("дан, ион, андрей")
if b > c and c > a:
    print("андрей, дан, ион")
else:
     print("ион, дан, андрей")
