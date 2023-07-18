from fractions import Fraction

def integer_to_hex(num:int)-> str:
    """
    Преобразует целое число в его шестнадцатеричное строковое представление.

    Аргументы:
    - num (int): Целое число.

    Возвращает:
    - str: Шестнадцатеричное представление целого числа.
    """
    if num == 0:
        return "0"
    result = ""
    while num > 0:
        remainder = num % 16
        if remainder < 10:
            result = str(remainder) + result
        else:
            result = chr(ord('A') + remainder - 10) + result
        num = num // 16
    return result

def calculate_fraction(fraction1_str: str , fraction2_str: str):
    """
    Вычисляет сумму и произведение дробей.

    Аргументы:
    - fraction1_str (str): Строковое представление первой дроби в формате "a/b".
    - fraction2_str (str): Строковое представление второй дроби в формате "a/b".

    Возвращает:
    - tuple: Кортеж с результатами - сумма и произведение дробей в виде кортежей (числитель, знаменатель).
    """
    numerator1, denominator1 = map(int, fraction1_str.split('/'))
    numerator2, denominator2 = map(int, fraction2_str.split('/'))

    # Сумма дробей
    sum_numerator = numerator1 * denominator2 + numerator2 * denominator1
    sum_denominator = denominator1 * denominator2

    # Произведение дробей
    product_numerator = numerator1 * numerator2
    product_denominator = denominator1 * denominator2

    return (sum_numerator, sum_denominator), (product_numerator, product_denominator)

def program_1():
    """
    Программа 1: Шестнадцатеричное представление целого числа.
    """
    num = int(input("Введите целое число: "))
    hex_string = integer_to_hex(num)
    print("Шестнадцатеричное представление:", hex_string)

    expected_hex_string = hex(num)[2:]
    if hex_string == expected_hex_string:
        print("Результат верный.")
    else:
        print("Результат неверный. Ожидаемый результат:", expected_hex_string)
        print("Проверка с помощью hex:", hex(num))

def program_2():
    """
    Программа 2: Сумма и произведение дробей.
    """
    fraction1_str = input("Введите первую дробь в формате a/b: ")
    fraction2_str = input("Введите вторую дробь в формате a/b: ")

    numerator1, denominator1 = map(int, fraction1_str.split('/'))
    numerator2, denominator2 = map(int, fraction2_str.split('/'))

    fraction1 = (numerator1, denominator1)
    fraction2 = (numerator2, denominator2)

    sum_fraction, product_fraction = calculate_fraction(fraction1, fraction2)

    print("Сумма дробей:", sum_fraction[0], "/", sum_fraction[1])
    print("Произведение дробей:", product_fraction[0], "/", product_fraction[1])

    expected_sum_fraction = Fraction(fraction1_str) + Fraction(fraction2_str)
    expected_product_fraction = Fraction(fraction1_str) * Fraction(fraction2_str)

    if sum_fraction == (expected_sum_fraction.numerator, expected_sum_fraction.denominator) and product_fraction == (expected_product_fraction.numerator, expected_product_fraction.denominator):
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
        if choice == "1":
            program_1()
        elif choice == "2":
            program_2()
        elif choice == "0":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
