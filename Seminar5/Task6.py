# Создание генератора таблицы умножения
multiplication_table = ((i, j, i*j) for i in range(2, 10) for j in range(2, 11))

# Вывод таблицы умножения
for i, j, result in multiplication_table:
    print(f"{i}x{j}={result}", end="  " if j < 10 else "\n")
