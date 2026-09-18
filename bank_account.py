# Проект простой банковский счет


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            print('Недостаточно средств!')
    def get_balance(self):
        print(f'Баланс владельца {self.owner}: {self.balance} руб.')
account = BankAccount('Artem')
account.deposit(1000)
account.withdraw(500)
account.get_balance()
account.withdraw(2000)
