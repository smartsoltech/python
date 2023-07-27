# Сохранение строки текста в переменной
text = "Hello, World!"

# Создание словаря, где ключ — буква, а значение — код буквы.
# Преобразование словаря в одну строку
char_code_dict_str = str({char: ord(char) for char in text})

print(char_code_dict_str)
