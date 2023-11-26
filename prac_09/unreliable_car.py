# Assuming the Car class is defined in car.py and is in the same directory
from car import Car
import random

class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car only if a random number is less than the car's reliability."""
        if random.randint(0, 100) < self.reliability:
            # If the number is less, the car will drive
            distance_driven = super().drive(distance)
        else:
            # If the number is not less, the car does not drive
            distance_driven = 0
        return distance_driven

