name = "John"
age = 30

# Простое форматирование
message = f"My name is {name} and I am {age} years old."
print(message)

# Выравнивание текста
title = "Python Programming"
formatted_title = f"{title:^30}"  # Выравнивание по центру
print(formatted_title)

formatted_title = f"{title:>60}"  # Выравнивание по правому краю
print(formatted_title)

formatted_title = f"{title:<30}"  # Выравнивание по левому краю
print(formatted_title)
