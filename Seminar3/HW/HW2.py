from collections import Counter
import re

def find_most_common_words(text: str, numbers: int):
    """Считает количество самых частых слов в строке

    Args:
        text (str): Исходная строка
        numbers (int): Количество слов

    Returns:
       tuple: Кортеж слов и количество вхождений
    """
    words = re.findall(r'\b\w+\b', text.lower())
    counter = Counter(words)
    return counter.most_common(numbers)

# Пример использования:
text = "Here is a simple text string. It contains some words. Some words appear more than once, some only once."
n = int(input("Количество: "))
print(find_most_common_words(text, n))  # Выведет 10 самых частых слов
