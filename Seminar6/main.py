import Task2
import Task6
import Task7

def main():
    while True:
        print("\nМеню:")
        print("1. Игра 'Угадай число'")
        print("2. Игра 'Угадай загадку'")
        print("3. Проверка даты на валидность")
        print("4. Выход")
        
        choice = input("Введите номер выбранного пункта: ")
        
        if choice == "1":
            lower = int(input("Введите нижнюю границу: "))
            upper = int(input("Введите верхнюю границу: "))
            attempts = int(input("Введите количество попыток: "))
            Task2.guess_the_number(lower, upper, attempts)
        elif choice == "2":
            attempts = int(input("Введите количество попыток: "))
            Task6.riddles_game(attempts)
            Task6.print_results()
        elif choice == "3":
            date = input("Введите дату в формате DD.MM.YYYY: ")
            if Task7.is_valid_date(date):
                print("Дата валидна.")
            else:
                print("Дата невалидна.")
        elif choice == "4":
            print("Выход из программы")
            break
        else:
            print("Неверный ввод. Пожалуйста, попробуйте еще раз.")

if __name__ == "__main__":
    main()
