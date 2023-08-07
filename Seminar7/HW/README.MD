# Документация для Python скрипта переименования файлов

## Описание

Этот Python скрипт используется для массового переименования файлов в указанной директории. 

Скрипт переименовывает файлы, основываясь на ряде параметров, передаваемых в командной строке при запуске скрипта.

## Использование

Скрипт используется путем запуска из командной строки с указанием параметров. 

Пример команды:

```
python main.py --wanted_name sample --count_nums 3 --extension_old .py --extension_new .py --diapazon 0 4 --directory /path/to/your/directory
```

Запуск:
```
python main.py -h
```

Результат
```
usage: main.py [-h] --wanted_name WANTED_NAME --count_nums COUNT_NUMS --extension_old EXTENSION_OLD --extension_new EXTENSION_NEW --diapazon DIAPAZON DIAPAZON [--directory DIRECTORY]

Rename files in a directory.

options:
  -h, --help            show this help message and exit
  --wanted_name WANTED_NAME
                        Desired final name of the files
  --count_nums COUNT_NUMS
                        Number of digits in the ordinal number
  --extension_old EXTENSION_OLD
                        Extension of the original file
  --extension_new EXTENSION_NEW
                        Extension of the final file
  --diapazon DIAPAZON DIAPAZON
                        Range of the original file name to keep
  --directory DIRECTORY
                        Directory to rename files in
```

## Параметры

- `-h` : Вывести справку по работе скрипта.

- `--wanted_name`: Желаемое конечное имя файлов. Это имя будет присвоено всем файлам в указанной директории, которые соответствуют другим параметрам. 

- `--count_nums`: Количество цифр в порядковом номере. Это определяет, сколько цифр будет в номере, добавленном к имени файла. Например, если `count_nums = 3`, номера будут выглядеть как 001, 002, 003 и т.д.

- `--extension_old`: Расширение исходного файла. Скрипт будет переименовывать только те файлы, которые имеют это расширение.

- `--extension_new`: Расширение конечного файла. После переименования файлы будут иметь это расширение.

- `--diapazon`: Диапазон сохраняемого оригинального имени. В скобках указываются начальная и конечная позиции символов в оригинальном имени, которые нужно сохранить. Например, `--diapazon 0 4` сохранит первые 4 символа оригинального имени.

- `--directory`: Директория, где находятся файлы. Укажите путь к директории, где находятся ваши файлы. Если параметр не указан, скрипт будет работать с текущей директорией.

## Примечание

Скрипт в текущем виде не поддерживает несколько расширений файлов одновременно. Для обработки всех файлов с одним и тем же именем, но разными расширениями, скрипт нужно запустить несколько раз: один раз для каждого расширения.