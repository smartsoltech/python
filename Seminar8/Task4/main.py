import os
import json
import pickle
import sys

def json_to_pickle(directory):
    # Обход файлов в директории
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Если файл имеет расширение .json
            if file.endswith(".json"):
                json_path = os.path.join(root, file)
                
                # Загрузка данных из JSON файла
                with open(json_path, 'r', encoding='utf-8') as json_file:
                    data = json.load(json_file)
                
                # Сохранение данных в формате pickle
                pickle_path = os.path.join(root, os.path.splitext(file)[0] + ".pkl")
                with open(pickle_path, 'wb') as pickle_file:
                    pickle.dump(data, pickle_file)
                
                print(f"Файл {json_path} был сохранен в формате pickle как {pickle_path}.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Пожалуйста, укажите путь к директории как аргумент.")
        sys.exit(1)
    
    directory = sys.argv[1]
    json_to_pickle(directory)
