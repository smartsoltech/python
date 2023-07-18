from fractions import Fraction

def integer_to_hex(num):
    return hex(num)[2:]

def calculate_fraction(input_string):
    numerator, denominator = map(int, input_string.split('/'))
    fraction = Fraction(numerator, denominator)
    return fraction

def program_1():
    num = int(input("Введите целое число: "))
    hex_string = integer_to_hex(num)
    print("Шестнадцатеричное представление:", hex_string)
    print("Проверка:", hex(num))

    expected_hex_string = hex(num)[2:]
    if hex_string == expected_hex_string:
        print("Результат верный.")
    else:
        print("Результат неверный. Ожидаемый результат:", expected_hex_string)

def program_2():
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
