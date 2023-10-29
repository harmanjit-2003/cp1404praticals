class ProgrammingLanguage:
    """Represent a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance.

        :param name: str, the name of the programming language
        :param typing: str, the type of typing of the programming language ("Static" or "Dynamic")
        :param reflection: bool, whether the programming language supports reflection
        :param year: int, the year the programming language first appeared
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the programming language is dynamically typed, else return False."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a string representation of the ProgrammingLanguage instance."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
