# Введенная пользователем строка
user_input = "Hello, world! This is a test string for Python."

# Создаем словарь для хранения частоты каждого символа
frequency_dict1 = {}

# Проходим по каждому символу в строке
for char in user_input:
    if char in frequency_dict1:
        frequency_dict1[char] += 1
    else:
        frequency_dict1[char] = 1

print(frequency_dict1)

#Используем count
# Введенная пользователем строка
user_input = "Hello, world! This is a test string for Python."

# Создаем словарь для хранения частоты каждого символа
frequency_dict = {}

# Проходим по каждому уникальному символу в строке
for char in set(user_input):
    frequency_dict[char] = user_input.count(char)

print(frequency_dict)