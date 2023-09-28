# Constants
MIN_LENGTH = 5  # TODO: Set the minimum password length
MAX_LENGTH = 15  # TODO: Set the maximum password length
REQUIRE_SPECIAL_CHAR = True  # TODO: Set whether special characters are required
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"  # TODO: Define the list of special characters

def main():
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("1 or more uppercase characters")
    print("1 or more lowercase characters")
    print("1 or more numbers")

    if REQUIRE_SPECIAL_CHAR:
        print(f"and 1 or more special characters: {SPECIAL_CHARACTERS}")

    while True:
        password = input("> ")
        if is_valid_password(password):
            print(f"Your {len(password)} character password is valid: {password}")
            break
        else:
            print("Invalid password!")

def is_valid_password(password):
    if MIN_LENGTH <= len(password) <= MAX_LENGTH:
        has_lowercase = False
        has_uppercase = False
        has_digit = False
        has_special_char = False

        for char in password:
            if char.islower():
                has_lowercase = True
            elif char.isupper():
                has_uppercase = True
            elif char.isdigit():
                has_digit = True
            elif REQUIRE_SPECIAL_CHAR and char in SPECIAL_CHARACTERS:
                has_special_char = True

        # TODO: Return True only if all criteria are met (lowercase, uppercase, digit, special_char)
        return has_lowercase and has_uppercase and has_digit and (not REQUIRE_SPECIAL_CHAR or has_special_char)

    # TODO: Handle the case where the password length is not within the specified range
    return False

if __name__ == "__main__":
    main()
