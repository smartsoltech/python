def calculate_profit(companies):
    all_profitable = True
    result = {}
    for company, transactions in companies.items():
        total = sum(transactions)
        result[company] = total
        if total < 0:
            all_profitable = False
    return result, all_profitable

companies = {
    "Company1": [1000, -500, 200, -300,],
    "Company2": [2000, -1000, 500, -500],
    "Company3": [1500, -700, 300, -200, -800,]
}

print(calculate_profit(companies))
