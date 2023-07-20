def find_duplicates(lst: list):
    """Сбор нового списка ищ дублирующихся элементов исходного списка

    Args:
        lst (list): Исходный список

    Returns:
        list: результирующий список
    """
    unique_elements = set()
    duplicates = set()
    for elem in lst:
        if elem in unique_elements:
            duplicates.add(elem)
        else:
            unique_elements.add(elem)
    return list(duplicates)

# Пример использования:
lst = [1, 2, 3, 1, 2, 3, 4, 5, 6, 4, 7, 8, 9, 7]
print(find_duplicates(lst))  # Выведет: [1, 2, 3, 4, 7]
