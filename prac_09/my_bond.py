class Band:
    def __init__(self, name):
        self.name = name
        self.musicians = []

    def add_musician(self, musician):
        self.musicians.append(musician)

    def play(self):
        """Simulate each musician playing their instrument."""
        for musician in self.musicians:
            if musician.instruments:  # If the musician has instruments
                for instrument in musician.instruments:
                    print(f"{musician.name} is playing: {instrument}")
            else:
                print(f"{musician.name} needs an instrument!")

    def __str__(self):
        """Return a string representation of the band and its musicians."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

# Assuming you have a Musician class defined with a name attribute and a list of instruments
class Musician:
    def __init__(self, name):
        self.name = name
        self.instruments = []

    def add_instrument(self, instrument):
        self.instruments.append(instrument)

    def __str__(self):
        """Return a string representation of the musician."""
        instruments_str = ', '.join(str(instrument) for instrument in self.instruments)
        return f"{self.name} ([{instruments_str}])"

# Assuming you have an Instrument class defined with name, year, and value attributes
class Instrument:
    def __init__(self, name, year, value):
        self.name = name
        self.year = year
        self.value = value

    def __str__(self):
        """Return a string representation of the instrument."""
        return f"{self.name} ({self.year}) : ${self.value:.2f}"
