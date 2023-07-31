import random

def guess_the_number(lower, upper, attempts):
    target = random.randint(lower, upper)
    for _ in range(attempts):
        guess = int(input("Введите ваше число: "))
        if guess == target:
            print("Поздравляем, вы угадали число!")
            return True
        elif guess < target:
            print("Ваше число меньше загаданного")
        else:
            print("Ваше число больше загаданного")
    print("К сожалению, ваши попытки закончились. Загаданное число было", target)
    return False
