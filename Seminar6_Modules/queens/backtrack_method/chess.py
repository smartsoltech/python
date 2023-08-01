# Константы
BOARD_SIZE = 8

def is_safe(board, row, col):
    """
    Проверяет, можно ли безопасно разместить ферзя на доске в указанной позиции.

    Аргументы:
    board: двумерный список, представляющий шахматную доску.
    row, col: целые числа, представляющие позицию (строка, столбец), которую следует проверить.

    Возвращает:
    True, если можно безопасно разместить ферзя в указанной позиции, и False в противном случае.
    """
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, BOARD_SIZE, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve(board, col):
    """
    Рекурсивно пытается разместить ферзей на шахматной доске.

    Аргументы:
    board: двумерный список, представляющий шахматную доску.
    col: целое число, представляющее текущую колонку.

    Возвращает:
    True, если все ферзи были успешно размещены, и False в противном случае.
    """
    if col >= BOARD_SIZE:
        return True
    for i in range(BOARD_SIZE):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve(board, col + 1) == True:
                return True
            board[i][col] = 0
    return False

def print_board(board):
    """
    Выводит шахматную доску на экран.

    Аргументы:
    board: двумерный список, представляющий шахматную доску.
    """
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            print(board[i][j], end=" ")
        print()

def solve_n_queens():
    """
    Решает задачу о восьми ферзях и выводит решение.

    Возвращает:
    True, если решение найдено, и False в противном случае.
    """
    board = [[0]*BOARD_SIZE for _ in range(BOARD_SIZE)]
    if solve(board, 0) == False:
        print("Solution does not exist")
        return False

    print_board(board)
    return True