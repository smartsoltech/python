
from itertools import combinations

def generate_combinations(items, max_weight):
    """Проверяет, сколько вещей и какаие именно влезут в рюкзак

    Args:
        items (dict): Список вещей с указанием веса каждой
        max_weight (float): Максимальная грузоподъемность рюкзака

    Returns:
        list: Список вещей,, которые могу войти в рюкзак
    """
    items_list = list(items.items())
    all_combinations = []
    
    for r in range(2, len(items_list) + 1):
        for combination in combinations(items_list, r):
            total_weight = sum(weight for _, weight in combination)
            if total_weight <= max_weight:
                all_combinations.append((total_weight, [item for item, _ in combination]))

    # Sort combinations by total weight in descending order
    all_combinations.sort(key=lambda x: x[0], reverse=True)

    return all_combinations

items = {
    "Тент": 10, "Вода": 3, "Еда": 2, "Одежда": 5, "аптечка": 1.5, 
    "носки": 0.5, "факел": 2, "спальный мешок": 4, "карта": 0.2, "компас": 0.1, 
    "нож": 0.7, "котелок": 1.2, "газовая горелка": 2.5, "дождевик": 0.8
}
max_weight = 25
combinations = generate_combinations(items, max_weight)

# Display the top 10 combinations
for i, (total_weight, items) in enumerate(combinations[:20], start=1):
    print(f"{i}. Общий вес вещей: {total_weight} кг, Комплектация рюкзака: {items}")
