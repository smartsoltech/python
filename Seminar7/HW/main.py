import os
import argparse

def rename(wanted_name, count_nums, extension_old, extension_new, diapazon, directory='.'):
    """
    Переименовывает файлы в указанной директории.

    Args:
        wanted_name (str): Желаемое конечное имя файлов.
        count_nums (int): Количество цифр в порядковом номере.
        extension_old (str): Расширение исходного файла.
        extension_new (str): Расширение конечного файла.
        diapazon (list): Диапазон сохраняемого оригинального имени.
        directory (str, optional): Директория, где находятся файлы. По умолчанию '.'.

    """
    # Список файлов в директории
    files = os.listdir(directory)
    
    # Счетчик переименованных файлов
    count = 1

    for filename in files:
        # Проверяем, что файл имеет нужное расширение
        if filename.endswith(extension_old):
            # Извлекаем часть оригинального имени
            original_name_part = filename[diapazon[0]:diapazon[1]]

            # Создаем новое имя файла
            new_name = f"{original_name_part}{wanted_name}{str(count).zfill(count_nums)}{extension_new}"

            # Полные пути к старому и новому файлам
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_name)

            # Переименовываем файл
            os.rename(old_file, new_file)

            # Увеличиваем счетчик
            count += 1

if __name__ == "__main__":
    """
    Основная точка входа в программу.
    Здесь обрабатываются аргументы командной строки и вызывается функция rename.
    """
    parser = argparse.ArgumentParser(description='Rename files in a directory.')
    parser.add_argument('--wanted_name', required=True, help='Desired final name of the files')
    parser.add_argument('--count_nums', type=int, required=True, help='Number of digits in the ordinal number')
    parser.add_argument('--extension_old', required=True, help='Extension of the original file')
    parser.add_argument('--extension_new', required=True, help='Extension of the final file')
    parser.add_argument('--diapazon', nargs=2, type=int, required=True, help='Range of the original file name to keep')
    parser.add_argument('--directory', default='.', help='Directory to rename files in')

    args = parser.parse_args()

    rename(args.wanted_name, args.count_nums, args.extension_old, args.extension_new, args.diapazon, args.directory)
