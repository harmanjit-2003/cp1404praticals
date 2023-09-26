import random

# Constants
MAX_SPICE = 1000
LOW_SPICE_THRESHOLD = 200

# Initial port cities
port_cities = ["Muziris", "Nelcynda", "Rhapta", "Sarapion"]
treasury = 0
years_simulated = 0


# Functions
def display_ports():
    print("\nYour trading connections:")
    print(", ".join(port_cities))


def add_new_port():
    global treasury
    while True:
        new_port_name = input("\nPort name: ").strip().title()
        if not new_port_name:
            print("Port name cannot be blank. Try again.")
        elif new_port_name in port_cities:
            print("You already have a connection to this port. Try again.")
        else:
            port_length = len(new_port_name)
            cost = port_length * 2  # Adjusted cost per letter for simplicity
            if treasury >= cost:
                treasury -= cost
                port_cities.append(new_port_name)
                print(f"You've added a new port: {new_port_name}")
                break
            else:
                print("You can't afford to add this port. Try again.")


def simulate_year():
    global years_simulated
    global treasury
    spice_trade = random.randint(0, MAX_SPICE)
    years_simulated += 1

    print(f"\nYear {years_simulated} simulation:")
    print(f"This year, the amount of spice traded was {spice_trade}.")

    if spice_trade < LOW_SPICE_THRESHOLD:
        if len(port_cities) > 1:
            removed_port = random.choice(port_cities)
            port_cities.remove(removed_port)
            print(f"Sadly, your connection of {removed_port} has been deleted.")
        else:
            print("All your trading connections have disappeared due to economic recession.")
            port_cities.clear()

    for city in port_cities:
        tax_revenue = int((random.uniform(0.5, 1.0) * spice_trade / 1000) * len(city))
        treasury += tax_revenue
        print(f"{city} earned {tax_revenue} sesterces.")


def main():
    print("Welcome to the Roman Spice Game!")
    print("You can create new port connections with the profits from trade.")
    print("Port connections cost and generate taxes according to name length.")
    print("For example, Nelcynda would cost 8 sesterces.")
    print("Trade brings in up to 1000 chests of spice per year.")
    print("If trade is less than 200 chests, you lose a trade connection.")
    print("You start with these ports: Muziris, Nelcynda, Rhapta, Sarapion")
    print("You start with these animals: Muziris, Nelcynda, Rhapta, Sarapion,")

    while True:
        print(
            f"After {years_simulated} years, you have {len(port_cities)} ports and your treasury has {treasury} sesterces.")
        print("(W)ait(D)isplay ports(A)dd new port(Q)uit")
        choice = input("Choose: ").strip().lower()

        if choice == 'w':
            simulate_year()
        elif choice == 'd':
            display_ports()
        elif choice == 'a':
            add_new_port()
        elif choice == 'q':
            if len(port_cities) > 0:
                print("\nYou finished with these ports:")
                display_ports()
            else:
                print("\nYou finished with no cities.")
            print(
                f"After {years_simulated} years, you have {len(port_cities)} ports and your treasury has {treasury} sesterces.")
            print("Thank you for playing the Roman Spice Game :)")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
