# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT) 

from random import randint

MIN_RANGE = 0
MAX_RANGE = 1000

def guess_number():
    """ Игра Угадай число
        Пользователь должен угадать загаданное компьютером число

    Returns:
        str: Ответ, угадал пользователь или нет
    """
    num = randint(MIN_RANGE, MAX_RANGE)
    attempts = 10
    while attempts > 0:
        guess = int(input("Введите число: "))
        if guess < num:
            print("Загаданное число больше")
        elif guess > num:
            print("Загаданное число меньше")
        else:
            return "Поздравляем, вы угадали число!"
        attempts -= 1
    return "Вы исчерпали все попытки. Загаданное число было " + str(num)

print(guess_number())
