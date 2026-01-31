n = int(input("enter n: "))

num_list = []
for _ in range(n):
    num = int(input())
    num_list.append(num)
    
min_num = min(num_list)
max_num = max(num_list)
    
print(f"min num {min_num}, max num {max_num}")