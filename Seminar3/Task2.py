def convert_input(user_input):
    # Попытка преобразования в целое число
    try:
        value = int(user_input)
        if value >= 0:
            return value
    except ValueError:
        pass

    # Попытка преобразования в вещественное число
    try:
        return float(user_input)
    except ValueError:
        pass

    # Попытка преобразования в строку в нижнем регистре
    if any(char.isupper() for char in user_input):
        return user_input.upper()
    else:
        return user_input.lower()

input_string = input('Введите что угодно: ')

print(f'{type(convert_input(input_string))}')