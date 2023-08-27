import argparse
import csv
import json
import math
import random

def quadratic_roots(a, b, c):
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

def generate_csv(filename, rows):
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for _ in range(rows):
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            c = random.randint(1, 10)
            csv_writer.writerow([a, b, c])
        print(f"Сгенерирован файл '{filename}' с {rows} строками.")

def load_equation_values_decorator(func):
    def wrapper(filename):
        with open(filename, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            rows = [row for row in csv_reader]
            if len(rows) < 1:
                print("Файл пуст.")
                return
            for row in rows:
                if len(row) != 3:
                    print("Неверное количество значений в строке. Должно быть 3 значения.")
                    continue
                a, b, c = map(int, row)
                result = func(a, b, c)
                print(f"Корни для {a=}, {b=}, {c=}: {result}")
    return wrapper

def save_to_json_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        data = {
            "args": args,
            "kwargs": kwargs,
            "result": result
        }
        with open("results.json", "a") as jsonfile:
            json.dump(data, jsonfile)
            jsonfile.write('\n')
        return result
    return wrapper

def main():
    parser = argparse.ArgumentParser(description="Решение квадратных уравнений")
    parser.add_argument("--a", type=float, help="Коэффициент 'a' в квадратном уравнении")
    parser.add_argument("--b", type=float, help="Коэффициент 'b' в квадратном уравнении")
    parser.add_argument("--c", type=float, help="Коэффициент 'c' в квадратном уравнении")
    parser.add_argument("--o", type=str, help="Открыть файл")
    parser.add_argument("--s", type=str, help="Сохранить в файл")
    parser.add_argument("--G", type=str, help="Сгенерировать CSV файл")
    parser.add_argument("--rows", type=int, default=100, help="Количество строк для генерации CSV файла")
    args = parser.parse_args()

    if args.G:
        generate_csv(args.G, args.rows)
    elif args.o:
        decorated_quadratic_roots = load_equation_values_decorator(quadratic_roots)
        decorated_quadratic_roots(args.o)
    elif args.a is not None and args.b is not None and args.c is not None:
        result = quadratic_roots(args.a, args.b, args.c)
        print(f"Корни для {args.a=}, {args.b=}, {args.c=}: {result}")
    elif args.s:
        result = quadratic_roots(args.a, args.b, args.c)
        with open(args.s, 'w') as f:
            f.write(f"Корни для {args.a=}, {args.b=}, {args.c=}: {result}\n")
        print(f"Результаты сохранены в файл {args.s}")
    else:
        print("Пожалуйста, укажите допустимые аргументы командной строки.")

if __name__ == "__main__":
    main()
