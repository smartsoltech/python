# Защищенный словарь для хранения результатов
_results = {}

def guess_the_riddle(riddle, possible_answers, attempts):
    print(f"Загадка: {riddle}")
    for i in range(attempts):
        guess = input("Введите ваш ответ: ")
        if guess in possible_answers:
            print("Поздравляем, вы отгадали загадку!")
            _results[riddle] = i + 1
            return i + 1
    print("К сожалению, ваши попытки закончились.")
    _results[riddle] = 0
    return 0

def riddles_game(attempts):
    riddles_dict = {
        "Что может в одно и то же время стоять и ходить, висеть и стоять, ходить и лежать?" : ["часы", "Часы"],
        "Без окон, без дверей, полна гостей." : ["яйцо", "Яйцо"],
        "На ноге – башмак, а в башмаке – никого." : ["гриб", "Гриб"],
        "Стоит домик, в нем два оконца.": ["нос", "Нос"],
        "Без рук, без ног, умеет молотить.": ["сердце", "Сердце"],
        "По полю течет, в реку не впадает.": ["дорога", "Дорога"],
        "Сидит дед во сто шуб одет.": ["капуста", "Капуста"],
        "Висит груша, нельзя скушать.": ["лампа", "Лампа"]
    }
    
    for riddle, answers in riddles_dict.items():
        if guess_the_riddle(riddle, answers, attempts) == 0:
            break


def print_results():
    print("\nРезультаты:")
    results_str = "\n".join(f"{riddle}: {'отгадана' if attempt else 'не отгадана'} на попытке {attempt if attempt else ''}" 
                            for riddle, attempt in _results.items())
    print(results_str)
