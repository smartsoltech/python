import chess

# Константы
NUMBER_OF_SOLUTIONS = 4

def main():
    """
    Главная функция, демонстрирующая использование chess.
    """
    solutions = chess.find_solutions(NUMBER_OF_SOLUTIONS)
    for i, solution in enumerate(solutions):
        print(f"Solution #{i + 1}: {solution}")

if __name__ == "__main__":
    main()
