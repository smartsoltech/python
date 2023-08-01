# main.py

import portfolio

stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
prices = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}

# Calculate the portfolio value
portfolio_value = portfolio.calculate_portfolio_value(stocks, prices)
print(f"Portfolio Value: {portfolio_value}")

# Calculate the portfolio return
initial_value = 10000.0
current_value = portfolio_value
portfolio_return = portfolio.calculate_portfolio_return(initial_value, current_value)
print(f"Portfolio Return: {portfolio_return}%")

# Get the most profitable stock
most_profitable_stock = portfolio.get_most_profitable_stock(stocks, prices)
print(f"Most Profitable Stock: {most_profitable_stock}")
