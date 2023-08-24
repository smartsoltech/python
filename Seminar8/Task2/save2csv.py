import json
import csv
import sys
import os

def save_json_to_csv(json_path):
    # Загрузка данных из JSON
    with open(json_path, 'r') as json_file:
        data = json.load(json_file)
    
    # Преобразование данных для сохранения в CSV
    csv_data = []
    for access_level, users in data.items():
        for identifier, name in users.items():
            csv_data.append([access_level, identifier, name])
    
    # Путь для сохранения CSV файла
    csv_path = os.path.join(os.path.dirname(json_path), "users.csv")
    
    # Сохранение данных в CSV
    with open(csv_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Access Level", "Identifier", "Name"])  # Заголовок CSV
        writer.writerows(csv_data)
    
    print("Данные сохранены в формате CSV.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Пожалуйста, укажите путь к файлу users.json как аргумент.")
        sys.exit(1)
    
    json_path = sys.argv[1]
    save_json_to_csv(json_path)


save_json_to_csv()