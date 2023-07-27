# Входные данные
names = ["John", "Sara", "Tom", "Anna"]
wages = [1000, 2000, 1500, 3000]
bonuses = ["10%", "5%", "20%", "15%"]

# Генератор словаря с именем в качестве ключа и суммой премии в качестве значения
bonus_dict = {name: wage * float(bonus.strip('%')) / 100 for name, wage, bonus in zip(names, wages, bonuses)}

print(bonus_dict)
