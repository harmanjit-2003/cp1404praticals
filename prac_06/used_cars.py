"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""


class Car:
    """Represent a Car object."""

    def __init__(self, name='', fuel=0):
        """Initialise a Car instance.

        name: str, name of the car
        fuel: float, one unit of fuel drives one kilometre
        """
        self.name = name
        self.fuel = fuel
        self._odometer = 0

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self._odometer += distance
        return distance

    def __str__(self):
        """Return a string representation of the car."""
        return f"{self.name}, fuel={self.fuel}, odometer={self._odometer}"


# Create a new Car object called "limo" that is initialised with 100 units of fuel.
limo = Car("Limo", 100)

# Add 20 more units of fuel to this new car object using the add method.
limo.add_fuel(20)

# Print the amount of fuel in the car.
print(f"Fuel in the car: {limo.fuel} units")  # Expected output: Fuel in the car: 120 units

# Attempt to drive the car 115 km using the drive method.
distance_driven = limo.drive(115)
print(f"The limo drove {distance_driven} km")  # Expected output: The limo drove 120 km

# Print the car's details using the __str__ method
print(limo)  # Expected output: Limo, fuel=0, odometer=120


# Creating more Car objects with names
sedan = Car("Sedan", 50)
truck = Car("Truck", 150)

# Add fuel, drive, and print details
sedan.add_fuel(25)
sedan.drive(30)
print(sedan)  # Expected output: Sedan, fuel=45, odometer=30

truck.drive(100)
print(truck)  # Expected output: Truck, fuel=50, odometer=100
