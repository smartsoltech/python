original_list = [1, 2, 3, 2, 1, 4, 5, 4, 6, 7, 6, 8, 8, 9, 10]
unique_list1 = list(set(original_list))

original_list = [1, 2, 3, 2, 1, 4, 5, 4, 6, 7, 6]
unique_list2 = []

for item in original_list:
    if item not in unique_list2:
        unique_list2.append(item)

print(f'Уникальный список. Короткий способ сортировки: {unique_list1}')
print(f'Длинный способ: {unique_list2}')