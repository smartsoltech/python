# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
# и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

MIN_RANGE = 0
MAX_RANGE = 10000

def check_prime(n: int) -> str:
    """Проверка числа на натуральность и простоту

    Args:
        int (n): User selected number

    Returns:
        str: Результат проверки введеного числа
    """
    if n <= MIN_RANGE or n > MAX_RANGE:
        return "Введенное число должно быть больше 0 и меньше 100000"
    if n == 1:
        return "Число 1 - не простое число"
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return "Число составное"
    return "Число простое"

n = int(input("Введите число: "))

print(check_prime(n))
