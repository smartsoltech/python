import os

# Функция для разделения пути к файлу на компоненты
def split_path(path):
    dirname, basename = os.path.split(path)
    filename, extension = os.path.splitext(basename)
    return dirname, filename, extension

# Пример использования функции
split_path("/home/user/documents/myfile.txt")
