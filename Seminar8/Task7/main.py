import csv
import pickle

def csv_to_pickle_str(csv_filename):
    data = []

    # Чтение CSV файла
    with open(csv_filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        headers = next(reader)  # Чтение заголовков
        for row in reader:
            data.append(dict(zip(headers, row)))

    # Преобразование данных в строку pickle
    pickle_str = pickle.dumps(data)

    return pickle_str

# Пример использования функции
pickle_result = csv_to_pickle_str("output.csv")  # Предполагаем, что файл называется "output.csv"
pickle_result
