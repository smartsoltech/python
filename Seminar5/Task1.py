# Константы
KEY1_POS = 1
KEY2_POS = 2
VALUE1_POS = 0
VALUE2_POS = 3

def form_dict(input_string: str) -> dict:
    """
    Функция, которая формирует словарь на основе входной строки, состоящей из четырех или более целых чисел, разделенных символом '/'.

    Args:
    input_string (str): Входная строка, состоящая из четырех или более целых чисел, разделенных символом '/'.

    Returns:
    dict: Словарь, в котором второе и третье число являются ключами, первое число является значением для первого ключа,
          четвертое и все последующие числа хранятся в кортеже как значения второго ключа.
    """
    numbers = list(map(int, input_string.split('/')))
    return {numbers[KEY1_POS]: numbers[VALUE1_POS], numbers[KEY2_POS]: tuple(numbers[VALUE2_POS:])}

print(form_dict('2/3/4/5/2/3/232/423/23'))