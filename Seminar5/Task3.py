# Сохранение строки текста в переменной
text = "Hello, World!"

# Создание словаря, где ключ — буква, а значение — код буквы.
# Преобразование словаря в одну строку
char_code_dict_str = str({char: ord(char) for char in text})

print(char_code_dict_str)

# Сохранение итератора словаря
char_code_dict = eval(char_code_dict_str)
dict_iterator = iter(char_code_dict.items())

# Вывод первых 5 пар ключ-значение
first_five_pairs = [next(dict_iterator) for _ in range(5)]
print(first_five_pairs)