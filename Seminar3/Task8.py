# Словарь с именами друзей и кортежами вещей
friends_dict = {
    "John": ("tent", "flashlight", "food", "water", "clothes"),
    "Mary": ("tent", "food", "water", "map", "compass"),
    "Steve": ("matches", "flashlight", "water", "clothes", "sunscreen"),
    "Lenny": ("Umbrella", "flashlight", "food", "water", "clothes"),
    "Jack": ("Umbrella", "food", "water", "map", "compass"),
    "Robert": ("Bike", "flashlight", "water", "clothes", "sunscreen")
}

# Преобразуем кортежи вещей в множества для удобства работы
friends_sets = {name: set(items) for name, items in friends_dict.items()}

# Вещи, которые взяли все три друга
all_items = set.intersection(*friends_sets.values())

# Вещи, которые уникальны для каждого друга
unique_items = {name: items - set.union(*(s for n, s in friends_sets.items() if n != name)) 
                for name, items in friends_sets.items()}

# Вещи, которые есть у всех друзей, кроме одного
one_missing_items = {name: (set.union(*(s for n, s in friends_sets.items() if n != name)) - items) 
                     for name, items in friends_sets.items()}

print(f'Все други: {all_items},\n Уникальные вещи: {unique_items}, \n Взял один: {one_missing_items}')
