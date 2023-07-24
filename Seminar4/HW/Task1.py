def transpose(matrix: dict):
    """Функця транспонирования матрицы

    Args:
        matrix (List): Передача матриццы для транспонирования

    Returns:
        List : Возвращенная транспонированная матрица
    """
    return [list(row) for row in zip(*matrix)]

matrix = [[1, 2, 3], [4, 5, 6]]
print(transpose(matrix))
