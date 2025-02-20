# 1
class Cart:
    def __init__(self, client):
        self.client = client
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def show_cart(self):
        print(f'Кошик клієнта {self.client}:', *self.items)


# cart = Cart("юзер1")
# cart.add_item("Хліб")
# cart.add_item("Шинка")
# cart.show_cart()
# cart.remove_item("Хліб")
# cart.show_cart()


# 2
class Phone:
    def __init__(self, number, battery=100):
        self.number = number
        self.battery = battery

    def reduce(self, percent):
        self.battery -= percent
        print(f"Залишилось: {self.battery}%")
        if self.battery < 20:
            print("Заряд менше 20%!")

    def info(self):
        print(f"Телефон {self.number} має заряд {self.battery}%")

# phone = Phone("+380", 67)
# phone.reduce(30)
# phone.reduce(30)
# phone.info()
