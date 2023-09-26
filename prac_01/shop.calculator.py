def main():
    while True:
        try:
            # Get the number of items from the user
            num_items = int(input("Number of items: "))

            # Check for a valid number of items
            if num_items < 0:
                print("Invalid number of items!")
                continue  # Ask for input again if it's invalid

            # Initialize total price
            total_price = 0

            # Get the price of each item and calculate the total
            for i in range(num_items):
                item_price = float(input("Price of item: $"))
                total_price += item_price

            # Apply discount if the total price is over $100
            if total_price > 100:
                total_price *= 0.9  # Apply 10% discount

            # Display the total price with 2 decimal places
            print(f"Total price for {num_items} items is ${total_price:.2f}")

            break  # Exit the loop if everything is successful

        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
