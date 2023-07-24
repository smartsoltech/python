def calculate_bonus(names: list, rates: list, bonuses: list) -> dict[str, int]:
    """Вычисление бонусов

    Args:
        names (list): Список получаталей бонуса
        rates (list): Оплата
        bonuses (list): Размер бонуса от Оплаты

    Returns:
        dict[str, int]: Список получателей бонуса с суммой бонуса
    """
    bonus_dict = {}
    for name, rate, bonus in zip(names, rates, bonuses):
        bonus_percent = float(bonus.strip('%')) / 100
        bonus_dict[name] = rate * bonus_percent
    return bonus_dict

names = ["Жека", "Васька", "Петька"]
rates = [1000, 1500, 1200]
bonuses = ["56%", "12.5345%", "7%"]

print(calculate_bonus(names, rates, bonuses))
