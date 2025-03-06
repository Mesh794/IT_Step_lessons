class Passenger:
    def __init__(self, name, destination):
        self.name = name
        self.destination = destination


class Transport:
    def __init__(self, speed):
        self.speed = speed

    def move(self, destination, distance):
        print(f"Відстань - {distance} км до {destination}, їхати - {distance / self.speed} год.")


class Bus(Transport):
    def __init__(self, speed, capacity, passengers=None):
        super().__init__(speed)
        self.passengers = [] if passengers is None else passengers
        self.capacity = capacity

    def board_passenger(self, passenger):
        if len(self.passengers) < self.capacity:
            print(f"Місце є")
            self.passengers.append(passenger)
        else:
            print(f"Місць нема")

    def move(self, destination, distance):
        departing = []
        newbees = []
        for passanger in self.passengers:
            if passanger.destination == destination:
                departing.append(passanger.name)
            else:
                newbees.append(passanger)
        self.passengers = newbees
        super().move(destination, distance)
        print("Висаджені:", *departing)


# bus1 = Bus(speed=50, capacity=3)
# p1 = Passenger("Ярослав1", "Київ")
# p2 = Passenger("Ярослав2", "Одеса")
# p3 = Passenger("Ярослав3", "Одеса")
# p4 = Passenger("Ярослав4", "Одеса")
# bus1.board_passenger(p1)
# bus1.board_passenger(p2)
# bus1.board_passenger(p3)
# bus1.board_passenger(p4)
# bus1.move("Київ", 600)
# bus1.move("Одеса", 800)
