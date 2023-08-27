import argparse
import csv
import json
import math
import random

# Константы
CSV_FILENAME = "coefficients.csv"
JSON_FILENAME = "results.json"
MIN_COEFFICIENT = 1
MAX_COEFFICIENT = 10

def load_equation_values_decorator(func):
    """Декоратор для загрузки значений уравнения из CSV файла"""
    def wrapper(filename, args):
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) == 3:
                    a, b, c = map(float, row)
                    result = func(a, b, c)
                    if args.s is not None:
                        save_to_json(a, b, c, result)
                else:
                    print(f"Строка '{','.join(row)}' не содержит 3 значения. Пропущена.")
    return wrapper

def save_to_json(a, b, c, result):
    """Сохраняет параметры и результаты работы функции в JSON файл"""
    data = {
        "a": a,
        "b": b,
        "c": c,
        "result": result
    }
    with open(JSON_FILENAME, "a") as jsonfile:
        json.dump(data, jsonfile)
        jsonfile.write('\n')

def generate_csv(filename, rows):
    """Генерирует CSV файл с случайными коэффициентами"""
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for _ in range(rows):
            a = random.randint(MIN_COEFFICIENT, MAX_COEFFICIENT)
            b = random.randint(MIN_COEFFICIENT, MAX_COEFFICIENT)
            c = random.randint(MIN_COEFFICIENT, MAX_COEFFICIENT)
            csv_writer.writerow([a, b, c])
        print(f"Сгенерирован файл '{filename}' с {rows} строками.")

def quadratic_roots(a, b, c):
    """Находит корни квадратного уравнения"""
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2 * a)
        return x
    else:
        return "Нет действительных корней"

def main():
    parser = argparse.ArgumentParser(description="Решение квадратных уравнений")
    parser.add_argument("--o", type=str, nargs="?", const=None, help="Открыть файл")
    parser.add_argument("--s", type=str, nargs="?", const=None, help="Сохранить в файл")
    parser.add_argument("--G", type=str, help="Сгенерировать CSV файл")
    parser.add_argument("--rows", type=int, default=100, help="Количество строк для генерации CSV файла")
    args = parser.parse_args()

    if args.G:
        generate_csv(args.G, args.rows)
        args.o = args.G

    if args.o is not None and args.s is not None:
        decorated_quadratic_roots = load_equation_values_decorator(quadratic_roots)
        decorated_quadratic_roots(args.o, args)
    elif args.o is not None:
        decorated_quadratic_roots = load_equation_values_decorator(quadratic_roots)
        decorated_quadratic_roots(args.o, args)
    elif args.s is not None:
        print("Пожалуйста, укажите файл с коэффициентами для вычисления корней.")
    else:
        print("Пожалуйста, укажите допустимые аргументы командной строки.")

if __name__ == "__main__":
    main()
