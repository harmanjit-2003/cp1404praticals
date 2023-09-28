import random

# Constants
STARTING_PRICE = 10.00
MIN_PRICE = 1.00
MAX_PRICE = 100.00
MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
OUTPUT_FILE = "stock_prices.txt"


def main():
    out_file = open(OUTPUT_FILE, 'w')

    price = STARTING_PRICE
    day = 0

    print(f"Starting price: ${price:,.2f}", file=out_file)

    while MIN_PRICE <= price <= MAX_PRICE:
        day += 1
        price_change = 0

        # 50% chance of increase, 50% chance of decrease
        if random.randint(0, 1) == 0:
            # Increase
            price_change = random.uniform(0, MAX_INCREASE)
        else:
            # Decrease
            price_change = -random.uniform(0, MAX_DECREASE)

        price *= (1 + price_change)
        price = round(price, 2)

        print(f"On day {day} price is: ${price:,.2f}", file=out_file)

    out_file.close()


if __name__ == "__main__":
    main()
