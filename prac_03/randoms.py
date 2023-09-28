# random.randint(5, 20):
#
# This line generates a random integer between 5 (inclusive) and 20 (inclusive).
# The smallest number you could have seen is 5.
# The largest number you could have seen is 20.
# random.randrange(3, 10, 2):
#
# This line generates a random integer from the range [3, 10) with a step of 2.
# The smallest number you could have seen is 3.
# The largest number you could have seen is 9.
# No, it couldn't have produced a 4 because the step is 2, so it only produces odd numbers in the given range.
# random.uniform(2.5, 5.5):
#
# This line generates a random floating-point number between 2.5 (inclusive) and 5.5 (inclusive).
# The smallest number you could have seen is 2.5.
# The largest number you could have seen is 5.5.
# To produce a random number between 1 and 100 inclusive, you can use the random.randint() function as follows:

random_number = random.randint(1, 100)
print(random_number)
