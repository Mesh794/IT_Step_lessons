from abc import abstractmethod


class Pet:
    def __init__(self, name, satiety=50, energy=50):
        self.name = name
        self.satiety = satiety
        self.energy = energy

    def sleep(self):
        self.energy = 100

    def eat(self, food_amount):
        self.satiety += min(self.satiety + food_amount, 100)

    @abstractmethod
    def play(self, activity_level):
        pass

    def make_sound(self):
        pass


class Cat(Pet):
    def play(self, activity_level):
        if self.satiety > 60:
            self.energy -= 2 * activity_level
            self.satiety -= activity_level

    def make_sound(self):
        print("Мяу")

    def catch_mouse(self):
        if self.energy > 30:
            print(f"{self.name} зловив мишу")
            if self.satiety > 40:
                print(f"{self.name} грається з мишею")
            else:
                print(f"{self.name} з'їв мишу")


class Dog(Pet):
    def play(self, activity_level):
        if self.satiety > 15:
            loss = activity_level // 2
            self.energy -= loss
            self.satiety -= loss

    def make_sound(self):
        print("Гав")

    def fetch_ball(self):
        if self.satiety > 10:
            print(f"{self.name} спіймав м'яч")
            self.energy -= 5
