from fractions import Fraction

def integer_to_hex(num):
    return hex(num)[2:]

def calculate_fraction(input_string):
    numerator, denominator = map(int, input_string.split('/'))
    fraction = Fraction(numerator, denominator)
    return fraction

def main():
    # Пример использования функции integer_to_hex
    num = int(input("Введите целое число: "))
    hex_string = integer_to_hex(num)
    print("Шестнадцатеричное представление:", hex_string)
    print("Проверка:", hex(num))

    # Пример использования функции calculate_fraction
    fraction1 = input("Введите первую дробь в формате a/b: ")
    fraction2 = input("Введите вторую дробь в формате a/b: ")

    # Сумма дробей
    sum_fraction = calculate_fraction(fraction1) + calculate_fraction(fraction2)
    # Произведение дробей
    product_fraction = calculate_fraction(fraction1) * calculate_fraction(fraction2)

    print("Сумма дробей:", sum_fraction)
    print("Произведение дробей:", product_fraction)

if __name__ == "__main__":
    main()
