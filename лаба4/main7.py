positive_nums = []
negative_nums = []

for _ in range(10):
    num = int(input())
    if num >= 0:
        positive_nums.append(num)
    else:
        negative_nums.append(num)

print(f"Count: {len(positive_nums)}, Summa: {sum(positive_nums)} of positive numbers")
print(f"Mean: {sum(negative_nums) / len(negative_nums)} of negative numbers")      
