"""
Доработайте класс `Vehicle`
"""

from abc import ABC
from homework_05.exceptions import LowFuelError, NotEnoughFuel

class Vehicle(ABC):
    def __init__(self, weight = 1950, fuel= 54, fuel_consumption = 10):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if not self.started:
            if self.fuel > 0:
                print(f'Start moving with {self.fuel} fuel.')
                self.started = True
            else:
                raise LowFuelError(self.fuel)
        else:
            print(f'Already started.')

    def move(self, distance):
        fuel_to_move = self.fuel_consumption * distance
        if fuel_to_move <= self.fuel:
            self.fuel = self.fuel - fuel_to_move
            print(f'Moved distance: {distance}. New fuel value: {self.fuel}.')
        else:
            raise NotEnoughFuel(distance)
