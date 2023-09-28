# Task 1: Write user's name to "name.txt"
user_name = input("Enter your name: ")

with open("name.txt", "w") as name_file:
    name_file.write(user_name)

# Task 2: Read the name from "name.txt" and print it
with open("name.txt", "r") as name_file:
    stored_name = name_file.read()
    print(f"Your name is {stored_name}")

# Task 3: Read and add the first two numbers from "numbers.txt"
with open("numbers.txt", "r") as numbers_file:
    line1 = int(numbers_file.readline())
    line2 = int(numbers_file.readline())
    total = line1 + line2
    print("Total of the first two numbers:", total)

# Task 4: Read and sum all numbers from "numbers.txt" (any number of numbers)
with open("numbers.txt", "r") as numbers_file:
    total = 0
    for line in numbers_file:
        total += int(line)

    print("Total of all numbers:", total)
