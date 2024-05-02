class Account():
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def deposit(self, money):
        if money > 0:
            self.balance += money
            print(f'Вы успешно пополнили счет. Сумма на счете {self.balance}')

    def withdraw(self, money):
        if money > self.balance:
            print (f'Недостаточно средств на счете')
        elif money <= self.balance:
            self.balance -= money
            print(f'Вы успешно обналичили {money} рублей. Остаток на счете: {self.balance} рублей.')

    def all_balance(self):
        print(f'Баланс счета {self.balance} рублей.')

man = Account('123456', 100000)

man.all_balance()
man.withdraw(10000)
man.deposit(2000)
man.all_balance()