from Guess_Number.Task3 import guess_the_number
from Guess_riddle.Task6 import riddles_game, print_results
from Date_validation.Task7 import is_valid_date
from Chess.chess import generate_queens

def main():
    while True:
        print("\nМеню:")
        print("1. Игра 'Угадай число'")
        print("2. Игра 'Угадай загадку'")
        print("3. Проверка даты на валидность")
        print("4. Сгенерировать безопасные расстановки ферзей")
        print("5. Выход")
        
        choice = input("Введите номер выбранного пункта: ")
        
        if choice == "1":
            lower = int(input("Введите нижнюю границу: "))
            upper = int(input("Введите верхнюю границу: "))
            attempts = int(input("Введите количество попыток: "))
            guess_the_number(lower, upper, attempts)
        elif choice == "2":
            attempts = int(input("Введите количество попыток: "))
            riddles_game(attempts)
            print_results()
        elif choice == "3":
            date = input("Введите дату в формате DD.MM.YYYY: ")
            if is_valid_date(date):
                print("Дата валидна.")
            else:
                print("Дата невалидна.")
        elif choice == "4":
            positions = generate_queens()
            for i, pos in enumerate(positions, start=1):
                print(f"Безопасная расстановка #{i}: {pos}")
        elif choice == "5":
            print("Выход из программы")
            break
        else:
            print("Неверный ввод. Пожалуйста, попробуйте еще раз.")

if __name__ == "__main__":
    main()
