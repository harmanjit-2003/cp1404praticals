CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}

print(CODE_TO_NAME)

while True:
    state_code = input("Enter short state: ").upper()  # Convert input to uppercase
    if state_code == "":
        break  # Exit the loop when Enter is pressed

    try:
        state_name = CODE_TO_NAME[state_code]
        print(f"{state_code} is {state_name}")
    except KeyError:
        print("Invalid short state")
