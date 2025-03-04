class CreditCardPayment:
    def __init__(self, currency):
        self.currency = currency

    def pay(self, amount):
        print(f"Оплата карткою {amount} {self.currency}")


class PayPalPayment:
    def __init__(self, currency):
        self.currency = currency

    def pay(self, amount):
        print(f"Оплата PayPal {amount} {self.currency}")


class CryptoPayment:
    def __init__(self, currency):
        self.currency = currency

    def pay(self, amount):
        print(f"Оплата криптогаманцем {amount} {self.currency}")


def create_payment():
    choice = input("1 - Кредитна картка, 2 - PayPal, 3 - Криптогаманець. Введіть номер варіанту: ")
    currency = input("Введіть валюту: ")
    if choice == '1':
        return CreditCardPayment(currency)
    elif choice == '2':
        return PayPalPayment(currency)
    elif choice == '3':
        return CryptoPayment(currency)
    else:
        print("Оберіть інший варіант")
        return None


accounts = []
accounts.append(create_payment())
accounts.append(create_payment())
accounts.append(create_payment())
for num, account in enumerate(accounts, start=1):
    account.pay(float(input(f"Введіть суму для оплати акаунту {num}: ")))
