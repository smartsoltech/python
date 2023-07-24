def calculate_bonus(names, rates, bonuses):
    bonus_dict = {}
    for name, rate, bonus in zip(names, rates, bonuses):
        bonus_percent = float(bonus.strip('%')) / 100
        bonus_dict[name] = rate * bonus_percent
    return bonus_dict

names = ["John", "Lisa", "Robert"]
rates = [1000, 1500, 1200]
bonuses = ["10%", "15%", "20%"]

print(calculate_bonus(names, rates, bonuses))
