from unreliable_car import UnreliableCar

def main():
    # Create a new UnreliableCar object with given name, fuel, and reliability
    my_unreliable_car = UnreliableCar("Old Faithless", 100, 50)

    # Attempt to drive the car for a distance
    distance_driven = my_unreliable_car.drive(30)
    print(f"Attempted to drive 30km and drove {distance_driven}km")

    # Print the car's details
    print(my_unreliable_car)

if __name__ == '__main__':
    main()
