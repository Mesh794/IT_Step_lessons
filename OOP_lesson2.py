class BankAccount:
    rates = {"UAH": 1, "USD": 39, "EUR": 42}

    def __init__(self, name, balance, currency):
        self.name = name
        self.balance = balance
        self.currency = currency
        self.check(currency)

    def show_info(self):
        print(f"Клієнт {self.name} має баланс {self.balance} {self.currency}")

    def check(self, currency):
        if currency not in self.rates:
            raise ValueError("Валюта невідома!")

    def convert(self, amount, initial, final):
        self.check(initial)
        self.check(final)
        return amount * self.rates[initial] / self.rates[final]

    def change_currency(self, new):
        self.check(new)
        self.balance = self.convert(self.balance, self.currency, new)
        self.currency = new
        print(f"Валюта змінена, баланс: {self.balance} {self.currency}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Баланс поповнено!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостатньо коштів!")
        else:
            self.balance -= amount
            print(f"Залишок: {self.balance} {self.currency}")

# account = BankAccount("test", 10000, "UAH")
# account.show_info()
# account.deposit(500)
# account.show_info()
# account.withdraw(200)
# account.change_currency("USD")
# account.change_currency("PLN")
