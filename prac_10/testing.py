"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest

# Assuming the Car class is defined in a separate module as specified
# from prac_06.car import Car

# Here's a mockup Car class definition for the sake of running this code.
# Replace it with the actual Car class from your 'prac_06.car' module.
class Car:
    def __init__(self, fuel=0):
        self.odometer = 0
        self.fuel = fuel

def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    # Fix the function so that it passes the assert test
    return " ".join([s] * n)

def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    # Fix the is_long_word function so that it passes the doctest
    return len(word) >= length

def format_phrase_as_sentence(phrase):
    """
    Format a phrase as a sentence - starting with a capital and ending with a single full stop.
    >>> format_phrase_as_sentence('hello')
    'Hello.'
    >>> format_phrase_as_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_phrase_as_sentence('good morning')
    'Good morning.'
    """
    # Capitalize the first letter and end with a single full stop.
    phrase = phrase.strip()
    if not phrase.endswith('.'):
        phrase += '.'
    return phrase[0].upper() + phrase[1:]

def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should now pass
    assert repeat_string("hi", 2) == "hi hi"

    # assert tests to show if Car sets the fuel correctly
    # Test with default fuel
    test_car = Car()
    assert test_car.fuel == 0, "Car default fuel should be 0"
    # Test with specified fuel
    test_car = Car(fuel=10)
    assert test_car.fuel == 10, "Car fuel should be set to 10"

# Uncomment the following line and run the doctests
doctest.testmod()

# Run the unit tests
run_tests()
