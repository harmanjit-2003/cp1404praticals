is_finished = False
result = None  # Initialize result to None to avoid "may be undefined" warning

while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        # TODO: this line
        is_finished = True  # Set is_finished to True to exit the loop when a valid integer is entered
    except ValueError:  # Catch a specific ValueError for invalid integer input
        print("Please enter a valid integer.")

print("Valid result is:", result)
