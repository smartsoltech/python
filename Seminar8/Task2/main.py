import json
import os

def add_user_to_db():
    filename = "./users.json"
    
    # Если файл существует, загружаем данные, иначе инициализируем пустой словарь
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
    else:
        data = {}
    
    try:
        while True:
            # Запрашиваем данные от пользователя
            name = input("Введите имя: ")
            identifier = input("Введите личный идентификатор: ")
            access_level = input("Введите уровень доступа (от 1 до 7): ")
            
            # Проверяем уникальность идентификатора
            if any(identifier in level_data for level_data in data.values()):
                print("Идентификатор уже существует. Попробуйте еще раз.")
                continue
            
            # Добавляем информацию в структуру данных
            if access_level not in data:
                data[access_level] = {}
            data[access_level][identifier] = name
            
            # Сохраняем обновленные данные в файл
            with open(filename, 'w') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

            print("Информация добавлена.")
    except KeyboardInterrupt:
        print("\nПрограмма прервана пользователем.")
    finally:
        # Убедимся, что перед выходом из программы данные сохраняются
        with open(filename, 'w') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print("Все данные сохранены.")

add_user_to_db()