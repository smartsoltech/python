# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print


# Константы для проверки диапазона чисел
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 999

number = int(input("Введите число от 1 до 999: "))

message = ""

if MINIMUM_NUMBER <= number <= MAXIMUM_NUMBER:
    if number < 10:  # однозначное число
        result = number ** 2
        message = "Введена цифра, ее квадрат равен: {}".format(result)
    elif number < 100:  # двузначное число
        first_digit = number // 10
        second_digit = number % 10
        result = first_digit * second_digit
        message = "Введено двузначное число, произведение его цифр равно: {}".format(result)
    else:  # трехзначное число
        reversed_number = int(str(number)[::-1])
        message = "Введено трехзначное число, его обратное отображение: {}".format(reversed_number)
else:
    message = "Число не входит в диапазон от 1 до 999. Пожалуйста, введите новое число."

print(message)
