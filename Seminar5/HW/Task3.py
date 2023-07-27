# Функция-генератор чисел Фибоначчи
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Вывод первых 10 чисел Фибоначчи
print(list(fibonacci(10)))
