"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")


# A ValueError will occur if the user enters something that cannot be converted to an integer when the program tries to execute int(input(...)). For example, if the user enters a non-integer value like "abc" or if they leave the input blank.
#
# A ZeroDivisionError will occur if the user enters 0 as the denominator, causing division by zero when calculating fraction = numerator / denominator.
#
# To avoid the possibility of a ZeroDivisionError, you can add a conditional statement to check if the denominator is zero before performing the division.