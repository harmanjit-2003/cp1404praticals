class Guitar:
    """Represent a guitar."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance.

        :param name: str, name of the guitar
        :param year: int, year the guitar was made
        :param cost: float, cost of the guitar
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the age of the guitar."""
        current_year = 2023  # Update to the current year
        return current_year - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old, False otherwise."""
        return self.get_age() >= 50
