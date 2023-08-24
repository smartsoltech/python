import csv
import json
import hashlib
import sys
import os

def process_csv_to_json(input_csv, output_json=None):
    # Чтение CSV-файла
    with open(input_csv, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)  # читаем заголовки CSV
        
        data = []
        for row in reader:
            # Дополнение ID нулями
            row[1] = row[1].zfill(10)
            
            # Преобразование имени
            row[2] = row[2].capitalize()
            
            # Создание хеша на основе имени и ID
            hash_value = hashlib.sha256((row[2] + row[1]).encode()).hexdigest()
            
            entry = {
                headers[0]: row[0],
                headers[1]: row[1],
                headers[2]: row[2],
                "hash": hash_value
            }
            data.append(entry)
    
    # Если имя выходного файла не указано, формируем его
    if not output_json:
        base_name, ext = os.path.splitext(input_csv)
        output_json = f"{base_name}_processed.json"
    
    # Сохранение данных в JSON-файл
    with open(output_json, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print("Обработка завершена. Данные сохранены в:", output_json)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Пожалуйста, укажите имя исходного CSV файла как аргумент.")
        sys.exit(1)
    
    input_csv = sys.argv[1]
    output_json = sys.argv[2] if len(sys.argv) > 2 else None
    process_csv_to_json(input_csv, output_json)
