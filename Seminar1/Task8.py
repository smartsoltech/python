# Нарисовать в консоли ёлку спросив
# у пользователя количество рядов.

rows = int(input("Введите количество рядов: "))

for i in range(1, rows + 1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))
    print(f'итерация цикла {i}')
