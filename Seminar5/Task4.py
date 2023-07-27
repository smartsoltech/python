# Создание генератора четных чисел от нуля до 100, исключая числа, сумма цифр которых равна 8
print (list(num for num in range(0, 101, 2) if sum(int(digit) for digit in str(num)) != 8))
