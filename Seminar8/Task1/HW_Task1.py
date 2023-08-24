import os
import json
import csv
import pickle
import sys

def get_directory_size(directory):
    """Возвращает размер директории в байтах, включая все вложенные файлы и директории."""
    total = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total += os.path.getsize(fp)
    return total

def recursive_directory_walk(directory):
    """Рекурсивно обходит директорию и возвращает информацию о файлах и директориях."""
    results = []

    for root, dirs, files in os.walk(directory):
        for name in files:
            filepath = os.path.join(root, name)
            size = os.path.getsize(filepath)
            results.append({
                "name": name,
                "parent": os.path.basename(root),
                "type": "file",
                "size": size
            })

        for name in dirs:
            dirpath = os.path.join(root, name)
            total_size = get_directory_size(dirpath)
            results.append({
                "name": name,
                "parent": os.path.basename(root),
                "type": "directory",
                "size": total_size
            })

    return results


def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def save_to_csv(data, filename):
    with open(filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "parent", "type", "size"])
        writer.writeheader()
        writer.writerows(data)

def save_to_pickle(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Пожалуйста, укажите путь к директории как аргумент.")
        sys.exit(1)

    directory = sys.argv[1]
    data = recursive_directory_walk(directory)

    save_to_json(data, "result.json")
    save_to_csv(data, "result.csv")
    save_to_pickle(data, "result.pkl")

    print("Обработка завершена. Результаты сохранены в: result.json, result.csv, result.pkl")
