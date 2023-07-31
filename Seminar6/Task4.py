def guess_the_riddle(riddle, possible_answers, attempts):
    print(f"Загадка: {riddle}")
    for i in range(attempts):
        guess = input("Введите ваш ответ: ")
        if guess in possible_answers:
            print("Поздравляем, вы отгадали загадку!")
            return i + 1
    print("К сожалению, ваши попытки закончились.")
    return 0
