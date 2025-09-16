"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""
class LowFuelError(Exception):
    def __init__(self, fuel):
        self.fuel = fuel

    def __str__(self):
        print(f'Fuel is low: {self.fuel}. Can\'t start moving')

class NotEnoughFuel(Exception):
    def __init__(self, distance):
        self.distance = distance

    def __str__(self):
        print(f'There is not enough fuel for distance: {self.distance}. Can\'t move')

class CargoOverload(Exception):
    def __init__(self, cargo):
        self.cargo = cargo

    def __str__(self):
        print(f'There is an overload for cargo: {self.cargo}. Can\'t fly')