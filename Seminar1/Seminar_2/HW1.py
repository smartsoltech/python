from fractions import Fraction

def integer_to_hex(number: int):
    """
    Преобразует целое число в его шестнадцатеричное строковое представление.

    Аргументы:
    - num (int): Целое число.

    Возвращает:
    - str: Шестнадцатеричное представление целого числа.
    """
    return hex(number)[3:]

def calculate_fraction(input_string: str):
    """
    Вычисляет дробь на основе входной строки в формате "a/b".

    Аргументы:
    - input_string (str): Входная строка в формате "a/b", где a - числитель, b - знаменатель.

    Возвращает:
    - Fraction: Результат дроби, представленный в виде объекта Fraction из модуля fractions.
    """
# Разбор строк на числитель и знаменатель
    numerator, denominator = map(int, input_string.split('/'))
    fraction = Fraction(numerator, denominator)
    return fraction

def program_1():
    """
    Программа 1: Шестнадцатеричное представление целого числа.
    """
    num = int(input("Введите целое число: "))
    hex_string = integer_to_hex(num)
    print("Шестнадцатеричное представление:", hex_string)
    print("Проверка:", hex(num))

    expected_hex_string = '0x' + hex(num)[2:]
    if hex_string == expected_hex_string:
        print("Результат верный.")
    else:
        print("Результат неверный. Ожидаемый результат:", expected_hex_string)

def program_2():
    """
    Программа 2: Сумма и произведение дробей.
    """
    fraction1 = input("Введите первую дробь в формате a/b: ")
    fraction2 = input("Введите вторую дробь в формате a/b: ")

    sum_fraction = calculate_fraction(fraction1) + calculate_fraction(fraction2)
    product_fraction = calculate_fraction(fraction1) * calculate_fraction(fraction2)
    
    print("Сумма дробей:", sum_fraction)
    print("Произведение дробей:", product_fraction)

    expected_sum_fraction = Fraction(fraction1) + Fraction(fraction2)
    expected_product_fraction = Fraction(fraction1) * Fraction(fraction2)
    if sum_fraction == expected_sum_fraction and product_fraction == expected_product_fraction:
        print("Результат верный.")
    else:
        print("Результат неверный.")
        print("Ожидаемая сумма:", expected_sum_fraction)
        print("Ожидаемое произведение:", expected_product_fraction)

def main():
    while True:
        print("Меню:")
        print("1 - Программа 1: Шестнадцатеричное представление целого числа")
        print("2 - Программа 2: Сумма и произведение дробей")
        print("0 - Выход")

        choice = input("Выберите программу (введите номер): ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                program_1()
            elif choice == 2:
                program_2()
            elif choice == 0:
                break
            else:
                print("Неверный выбор. Попробуйте снова.")
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
