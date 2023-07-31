import random
import argparse

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Игра 'Угадай число'")
    parser.add_argument("params", metavar="N", type=int, nargs="*", help="параметры вызова функции")
    args = parser.parse_args()
    
    lower = 1
    upper = 100
    attempts = 10
    
    if len(args.params) > 0:
        lower = args.params[0]
    if len(args.params) > 1:
        upper = args.params[1]
    if len(args.params) > 2:
        attempts = args.params[2]
    
    guess_the_number(lower, upper, attempts)
