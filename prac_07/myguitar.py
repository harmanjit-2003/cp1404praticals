import csv

class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = int(year)
        self.cost = float(cost)

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        return self.year < other.year


def load_guitars(filename):
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            guitars.append(Guitar(*row))
    return guitars


def save_guitars(filename, guitars):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


def main():
    filename = 'guitars.csv'
    guitars = load_guitars(filename)

    print("These are my guitars:")
    for guitar in guitars:
        print(guitar)

    guitars.sort()
    print("\nSorted by year:")
    for guitar in guitars:
        print(guitar)

    add_more = input("Would you like to add more guitars? (Y/n) ").lower()
    while add_more != 'n':
        name = input("Name: ")
        year = input("Year: ")
        cost = input("Cost: ")
        guitars.append(Guitar(name, year, cost))
        add_more = input("Add another? (Y/n) ").lower()

    save_guitars(filename, guitars)
    print("Guitars saved.")


if __name__ == '__main__':
    main()
