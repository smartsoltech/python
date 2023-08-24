import pickle
import csv

def pickle_to_csv(pickle_filename, csv_filename):
    # Шаг 1: Загрузка данных из pickle файла
    with open(pickle_filename, 'rb') as pkl_file:
        data = pickle.load(pkl_file)

    # Шаг 2: Извлечение ключей для заголовков CSV
    headers = data[0].keys()

    # Шаг 3: Запись данных в CSV файл
    with open(csv_filename, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

    return f"Data has been successfully written to {csv_filename}"


pickle_to_csv("result.pkl", "users.csv")
