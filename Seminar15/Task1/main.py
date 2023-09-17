
import pandas as pd
import yaml
import re
import argparse
import logging

def load_keywords_from_yaml(file_path):
    """
    Загружает ключевые слова из YAML-файла.

    Параметры:
    - file_path (str): Путь к YAML-файлу.

    Возвращает:
    - dict: Словарь с категориями и ключевыми словами.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        logging.error(f"Ошибка при чтении YAML-файла: {e}")
        return None

def categorize_emails(df, categories_keywords):
    """
    Категоризирует письма на основе ключевых слов.

    Параметры:
    - df (DataFrame): DataFrame с письмами.
    - categories_keywords (dict): Словарь с категориями и ключевыми словами.

    Возвращает:
    - DataFrame: DataFrame с категоризированными письмами.
    """
    categorized_df = df.copy()
    for category in categories_keywords:
        categorized_df[category] = 0

    for index, row in df.iterrows():
        email_content = row['E-mail'].lower()
        for category, keywords in categories_keywords.items():
            for keyword in keywords:
                if re.search(r'\b' + re.escape(keyword) + r'\b', email_content):
                    categorized_df.at[index, category] = 1

    return categorized_df

def main(input_csv, output_csv, yaml_file):
    """
    Основная функция для категоризации писем.

    Параметры:
    - input_csv (str): Путь к входному CSV-файлу.
    - output_csv (str): Путь к выходному CSV-файлу.
    - yaml_file (str): Путь к YAML-файлу с ключевыми словами.
    """
    # Настройка логирования
    logging.basicConfig(filename='email_categorizer.log', level=logging.INFO)

    try:
        df = pd.read_csv(input_csv, header=None, names=['E-mail'])
    except Exception as e:
        logging.error(f"Ошибка при чтении CSV-файла: {e}")
        return

    categories_keywords = load_keywords_from_yaml(yaml_file)
    if categories_keywords is None:
        return

    try:
        categorized_df = categorize_emails(df, categories_keywords)
        categorized_df.to_csv(output_csv, index=False)
        logging.info(f"Категоризация успешно завершена. Результаты сохранены в {output_csv}.")
    except Exception as e:
        logging.error(f"Ошибка при категоризации писем: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Категоризация писем по ключевым словам.')
    parser.add_argument('--input', type=str, required=True, help='Путь к входному CSV-файлу.')
    parser.add_argument('--output', type=str, required=True, help='Путь к выходному CSV-файлу.')
    parser.add_argument('--yaml', type=str, required=True, help='Путь к YAML-файлу с ключевыми словами.')

    args = parser.parse_args()
    main(args.input, args.output, args.yaml)
