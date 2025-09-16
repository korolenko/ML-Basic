"""
Создайте класс `Car`, наследник `Vehicle`
"""
from homework_05.base import Vehicle
from homework_05.engine import Engine


class Car(Vehicle):
    def __init__(self):
        self._engine = Engine(239,4)
        super().__init__()

    def set_engine(self, engine: Engine):
        self._engine = engine
