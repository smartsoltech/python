import csv
import pickle

def pickle_to_csv(pickle_file, csv_file):
    # Загрузка данных из pickle файла
    with open(pickle_file, 'rb') as f:
        data = pickle.load(f)
    
    # Извлекаем ключи словаря для заголовков CSV
    headers = data[0].keys()

    # Сохранение данных в CSV
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

    print(f"Data from {pickle_file} saved to {csv_file}")

pickle_to_csv("./sample_data.pkl", "output.csv")
