class ProgrammingLanguage:
    """Represent information about a programming language including whether it supports pointer arithmetic."""

    def __init__(self, name, typing, reflection, year, pointer_arithmetic):
        """
        Construct a ProgrammingLanguage from the given values.

        :param name: str - The name of the programming language
        :param typing: str - The typing discipline (Static or Dynamic)
        :param reflection: bool - Indicates if the language supports reflection
        :param year: int - The year the language first appeared
        :param pointer_arithmetic: bool - Indicates if the language supports pointer arithmetic
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def __str__(self):
        """Return a string representation of a ProgrammingLanguage."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, Pointer Arithmetic={self.pointer_arithmetic}, First appeared in {self.year}"

    def __repr__(self):
        """Return a string that is a valid Python expression that could be used to recreate an object with the same state."""
        return (f"{self.__class__.__name__}("
                f"'{self.name}', '{self.typing}', {self.reflection}, {self.year}, {self.pointer_arithmetic})")

    def is_dynamic(self):
        """Determine if the language is dynamically typed."""
        return self.typing == "Dynamic"


def run_tests():
    """Run tests on ProgrammingLanguage class."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995, False)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991, False)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991, False)
    c = ProgrammingLanguage("C", "Static", False, 1972, True)  # Adding a new language with pointer arithmetic

    languages = [ruby, python, visual_basic, c]
    print(python)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language)

    print("\nLanguages that support pointer arithmetic are:")
    for language in languages:
        if language.pointer_arithmetic:
            print(language.name)


if __name__ == "__main__":
    run_tests()
