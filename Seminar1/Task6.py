# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print



# Константы для проверки високосности года
CHECK_DIVISIBLE_BY_4 = 4
CHECK_DIVISIBLE_BY_100 = 100
CHECK_DIVISIBLE_BY_400 = 400
START_OF_GREGORIAN_CALENDAR = 1582

year = int(input("Введите год: "))

if year < START_OF_GREGORIAN_CALENDAR:
    print("Григорианский календарь начинается с 1582 года. Пожалуйста, введите год после 1582.")
elif year % CHECK_DIVISIBLE_BY_4 == 0:
    if year % CHECK_DIVISIBLE_BY_100 == 0:
        if year % CHECK_DIVISIBLE_BY_400 == 0:
            print("Год {} является високосным.".format(year))
        else:
            print("Год {} не является високосным.".format(year))
    else:
        print("Год {} является високосным.".format(year))
else:
    print("Год {} не является високосным.".format(year))
