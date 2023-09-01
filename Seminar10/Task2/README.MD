# Документация для скрипта "Фабрика Животных"

## Описание

Этот скрипт предоставляет возможность создавать и управлять экземплярами животных с использованием аргументов командной строки.

## Использование

Вы можете запустить скрипт с помощью следующей команды:

```bash
python main.py <действие> [--type <тип_животного>] [--name <имя_животного>] [--attribute_name <атрибут>] [--attribute_value <значение>]
```

### Доступные действия

- `create`: Создать новый экземпляр животного.
- `attributes`: Добавить атрибуты существующему экземпляру животного.

### Доступные опции

- `--type`: Указать тип животного (например, cat, dog).
- `--name`: Указать имя животного.
- `--attribute_name`: Указать имя атрибута.
- `--attribute_value`: Указать значение атрибута.

## Примеры использования

1. Создание кошки с именем "Васька":
```bash
python main.py create --type cat --name Васька
```

2. Добавление атрибута к собаке с именем "Бобик":
```bash
python main.py attributes --type dog --name Бобик --attribute_name размер --attribute_value средний
```

3. Создание кошки с именем "Мурка" и добавление атрибутов:
```bash
python main.py create --type cat --name Мурка
python main.py attributes --type cat --name Мурка --attribute_name цвет --attribute_value белый
python main.py attributes --type cat --name Мурка --attribute_name возраст --attribute_value 3
```

4. Создание собаки с именем "Шарик", добавление атрибутов и издание звука барка:
```bash
python main.py create --type dog --name Шарик
python main.py attributes --type dog --name Шарик --attribute_name порода --attribute_value йоркширский_терьер
python main.py attributes --type dog --name Шарик --attribute_name возраст --attribute_value 5
```

Используйте эти примеры, чтобы понять, как использовать скрипт с разными опциями и действиями.
```

Вы можете использовать этот пример для создания полной документации на русском языке для вашего скрипта в формате MarkDown. Замените placeholder'ы на реальные описания, примеры и спецификации.