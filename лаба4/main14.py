n = int(input("enter ur quantity of x'es: "))
a = int(input("enter ur number for comparison: "))

count = 0
# for i in range (n):
#     x = int(input("Enter your x: "))
#     if a == x:        
#         count += 1
    
for i in range(n):
    x = int(input())
    string_x = str(x)
    string_a = str(a)
    count_of_a_in_x = string_x.count(string_a) 
    count += count_of_a_in_x
    # count += str(x).count(str(a))
print(count)