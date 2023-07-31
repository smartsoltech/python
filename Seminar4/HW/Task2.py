def create_dict(**kwargs):
    """Функция упаковки словаря

    Returns:
        dict: Упакованный словарь
    """
    result = {}
    for key, value in kwargs.items():
        try:
            result[value] = key
        except TypeError:
            result[str(value)] = key
    return result

print(create_dict(a=1, b='2', c=[3, 4, 5]))
