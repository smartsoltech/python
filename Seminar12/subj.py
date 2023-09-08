# Для начала создадим пример файла CSV с названиями предметов
import csv

# Пример названий предметов
subjects = ["Mathematics", "Physics", "Chemistry", "History", "Literature"]

# Сохранение в файл CSV
csv_file_path = "subjects.csv"
with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Subjects"])
    for subject in subjects:
        writer.writerow([subject])

csv_file_path
