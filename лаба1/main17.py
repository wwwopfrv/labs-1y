hours = int(input("введите время начало урока(ч):"))
minutes = int(input("введите время начало урока(мин):"))
sum_minutes = hours * 60 + minutes + 7 * 45 + 15 * 2 + 10 * 4
print(sum_minutes // 60, sum_minutes % 60)
