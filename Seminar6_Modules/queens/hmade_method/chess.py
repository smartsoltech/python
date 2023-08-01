# chess.py

import random
from tqdm import tqdm

# Константы
BOARD_SIZE = 8

def is_solution(queens):
    """
    Проверяет, является ли данная расстановка ферзей решением задачи.

    Аргументы:
    queens: Список кортежей, где каждый кортеж содержит координаты ферзя.

    Возвращает:
    True, если данная расстановка является решением задачи, и False в противном случае.
    """
    for i in range(BOARD_SIZE):
        for j in range(i + 1, BOARD_SIZE):
            if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1] or abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                return False
    return True

def generate_random_solution():
    """
    Генерирует случайную расстановку ферзей.

    Возвращает:
    Список кортежей, где каждый кортеж содержит координаты ферзя.
    """
    queens = [(random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1)) for _ in range(BOARD_SIZE)]
    return queens



def find_solutions(n):
    """
    Ищет указанное количество решений задачи и возвращает их.

    Аргументы:
    n: Количество решений, которые нужно найти.

    Возвращает:
    Список расстановок, являющихся решениями задачи. Каждая расстановка представлена в виде списка кортежей.
    """
    solutions = []
    # Создаем индикатор прогресса с помощью tqdm
    with tqdm(total=n, desc="Finding solutions", unit="solution") as pbar:
        while len(solutions) < n:
            queens = generate_random_solution()
            if is_solution(queens):
                solutions.append(queens)
                # Обновляем индикатор прогресса каждый раз, когда находим решение
                pbar.update()
    return solutions
