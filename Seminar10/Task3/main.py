import os
import json
import csv
import pickle
import sys

class DirectoryProcessor:
    def __init__(self, directory):
        self.directory = directory
        self.data = []

    def get_directory_size(self, directory):
        """Возвращает размер директории в байтах, включая все вложенные файлы и директории."""
        total = 0
        for dirpath, dirnames, filenames in os.walk(directory):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total += os.path.getsize(fp)
        return total

    def recursive_directory_walk(self):
        """Рекурсивно обходит директорию и возвращает информацию о файлах и директориях."""
        for root, dirs, files in os.walk(self.directory):
            for name in files:
                filepath = os.path.join(root, name)
                size = os.path.getsize(filepath)
                self.data.append({
                    "name": name,
                    "parent": os.path.basename(root),
                    "type": "file",
                    "size": size
                })

            for name in dirs:
                dirpath = os.path.join(root, name)
                total_size = self.get_directory_size(dirpath)
                self.data.append({
                    "name": name,
                    "parent": os.path.basename(root),
                    "type": "directory",
                    "size": total_size
                })

    def save_to_json(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)

    def save_to_csv(self, filename):
        with open(filename, 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["name", "parent", "type", "size"])
            writer.writeheader()
            writer.writerows(self.data)

    def save_to_pickle(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.data, file)

    def process(self):
        self.recursive_directory_walk()
        self.save_to_json("result.json")
        self.save_to_csv("result.csv")
        self.save_to_pickle("result.pkl")
        print("Обработка завершена. Результаты сохранены в: result.json, result.csv, result.pkl")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Пожалуйста, укажите путь к директории как аргумент.")
        sys.exit(1)

    directory = sys.argv[1]
    processor = DirectoryProcessor(directory)
    processor.process()
