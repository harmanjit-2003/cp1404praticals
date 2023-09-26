# Set the minimum password length
MIN_PASSWORD_LENGTH = 8

while True:
    password = input("Enter your password: ")

    if len(password) < MIN_PASSWORD_LENGTH:
        print(f"Password must be at least {MIN_PASSWORD_LENGTH} characters long. Try again.")
    else:
        print("*" * len(password))
        break
