# Given list
numbers = [3, 1, 4, 1, 5, 9, 2]

# Questions:
# 1. What values do the following expressions have?

# The first element of the list
numbers[0]  # Should be 3

# The last element of the list
numbers[-1]  # Should be 2

# The fourth element of the list
numbers[3]  # Should be 1

# All elements except the last one
numbers[:-1]  # Should be [3, 1, 4, 1, 5, 9]

# A slice from index 3 to 4 (exclusive)
numbers[3:4]  # Should be [1]

# Check if 5 is in the list
5 in numbers  # Should be True

# Check if 7 is in the list
7 in numbers  # Should be False

# Check if the string "3" is in the list
"3" in numbers  # Should be False

# Concatenate the list with [6, 5, 3]
numbers + [6, 5, 3]  # Should be [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Operations to perform:

# Change the first element of numbers to "ten"
numbers[0] = "ten"

# Change the last element of numbers to 1
numbers[-1] = 1

# Print all elements from numbers except the first two (slice)
print(numbers[2:])

# Print whether 9 is an element of numbers
print(9 in numbers)
