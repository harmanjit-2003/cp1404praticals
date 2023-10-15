def extract_name(email):
    # Split the email address at '@' to separate the username and domain
    parts = email.split('@')

    # Split the username into words
    words = parts[0].split('.')

    # Capitalize each word and join them to create the name
    name = ' '.join(word.title() for word in words)

    return name


# Create a dictionary to store emails and names
user_dict = {}

while True:
    email = input("Email: ")
    if email == "":
        break  # Exit the loop when Enter is pressed

    # Extract the name from the email
    name = extract_name(email)

    # Check if the name is correct
    confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
    if confirmation == '' or confirmation == 'y':
        user_dict[email] = name
    else:
        new_name = input("Name: ")
        user_dict[email] = new_name

# Print the names and emails
for email, name in user_dict.items():
    print(f"{name} ({email})")
