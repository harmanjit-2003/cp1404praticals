

def main():
    while True:
        try:
            # Get the user's sales amount as input
            sales = float(input("Enter sales: $"))

            # Check if the user entered a negative number to exit the loop
            if sales < 0:
                break

            # Determine the bonus based on sales amount
            if sales < 1000:
                bonus = sales * 0.10  # 10% bonus
            else:
                bonus = sales * 0.15  # 15% bonus

            # Display the calculated bonus
            print(f"Your bonus is: ${bonus:.2f}")

        except ValueError:
            print("Invalid input. Please enter a valid numeric sales amount.")

if __name__ == "__main__":
    main()
