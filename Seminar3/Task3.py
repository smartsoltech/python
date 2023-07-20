# Вручную создаем кортеж, содержащий элементы разных типов
my_tuple = (1, 2.0, "three", 4, 5.0, "six", 7, 8.0, "nine")

# Создаем словарь, где ключи - это типы данных, а значения - списки элементов этого типа
dict_of_lists = {}
for item in my_tuple:
    if type(item) in dict_of_lists:
        dict_of_lists[type(item)].append(item)
    else:
        dict_of_lists[type(item)] = [item]

print(dict_of_lists)
