MAX_DEPOSTI_AMOUNT = 5000000
AMOUNT_DEVIDER = 50
class ATM:
    def __init__(self):
        """Инициализация объекта
        """
        self.balance = 0
        self.operation_count = 0

    def deposit(self, amount):
        
        """Пополнение

        Returns:
            float: Баланс
        """
        if amount % AMOUNT_DEVIDER != 0:
            return "The amount should be a multiple of 50"
        if self.balance > MAX_DEPOSTI_AMOUNT:
            self.balance -= self.balance * 0.1
        self.balance += amount
        self.operation_count += 1
        self.add_interest()
        return self.balance

    def withdraw(self, amount):
        """Снятие денег

        Args:
            amount (_type_): Сумма снятия

        Returns:
            float: Оставшийся баланс
        """
        if amount % AMOUNT_DEVIDER != 0:
            return "The amount should be a multiple of 50"
        fee = max(min(amount * 0.015, 600), 30)
        if amount + fee > self.balance:
            return "Insufficient balance"
        if self.balance > MAX_DEPOSTI_AMOUNT:
            self.balance -= self.balance * 0.1
        self.balance -= amount + fee
        self.operation_count += 1
        self.add_interest()
        return self.balance

    def add_interest(self):
        if self.operation_count % 3 == 0:
            self.balance += self.balance * 0.03

atm = ATM()
print(atm.deposit(1050))
print(atm.withdraw(50))
print(atm.withdraw(50))
print(atm.deposit(1050))
print(atm.withdraw(50))
print(atm.withdraw(50))
print(atm.deposit(1050))
print(atm.withdraw(50)) 
print(atm.withdraw(50))
