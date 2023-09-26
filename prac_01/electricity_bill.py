# Define constants for tariffs
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

# Display a welcome message
print("Electricity bill estimator 2.0")

# Get the user's choice of tariff
tariff_choice = input("Which tariff? 11 or 31: ")

# Validate the user's input for tariff choice
while tariff_choice not in ('11', '31'):
    print("Invalid tariff choice. Please enter 11 or 31.")
    tariff_choice = input("Which tariff? 11 or 31: ")

# Convert the tariff choice to the appropriate rate
tariff_rate = TARIFF_11 if tariff_choice == '11' else TARIFF_31

# Get the daily use in kWh and number of billing days from the user
daily_use = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))

# Calculate the estimated bill
estimated_bill = tariff_rate * daily_use * billing_days

# Display the estimated bill with 2 decimal places
print(f"Estimated bill: ${estimated_bill:.2f}")
