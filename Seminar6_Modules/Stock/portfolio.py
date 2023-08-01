# portfolio.py

# Константы
STOCK_NOT_FOUND = "Stock not found"

def calculate_portfolio_value(stocks, prices):
    """
    Вычисляет общую стоимость портфеля акций.

    Аргументы:
    stocks: Словарь, где ключи - символы акций, а значения - количество акций.
    prices: Словарь, где ключи - символы акций, а значения - цены акций.

    Возвращает:
    Общую стоимость портфеля акций.
    """
    return sum(stocks[stock] * prices.get(stock, STOCK_NOT_FOUND) for stock in stocks)

def calculate_portfolio_return(initial_value, current_value):
    """
    Вычисляет доходность портфеля акций.

    Аргументы:
    initial_value: Начальная стоимость портфеля акций.
    current_value: Текущая стоимость портфеля акций.

    Возвращает:
    Процентную доходность портфеля.
    """
    return ((current_value - initial_value) / initial_value) * 100

def get_most_profitable_stock(stocks, prices):
    """
    Определяет наиболее прибыльную акцию.

    Аргументы:
    stocks: Словарь, где ключи - символы акций, а значения - количество акций.
    prices: Словарь, где ключи - символы акций, а значения - цены акций.

    Возвращает:
    Символ акции, которая имеет наибольшую прибыль по сравнению с ее начальной стоимостью.
    """
    profits = {stock: stocks[stock] * prices.get(stock, STOCK_NOT_FOUND) for stock in stocks}
    return max(profits, key=profits.get)
