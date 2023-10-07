import random

# Constants
MIN_NUMBER = 1
MAX_NUMBER = 45
NUM_QUICK_PICKS = 5
NUMBERS_PER_QUICK_PICK = 6

# Function to generate a single quick pick
def generate_quick_pick():
    return sorted(random.sample(range(MIN_NUMBER, MAX_NUMBER + 1), NUMBERS_PER_QUICK_PICK))

# Function to display quick picks
def display_quick_picks(quick_picks):
    for line in quick_picks:
        print(" ".join(map(str, line)))

def main():
    # Ask the user for the number of quick picks
    num_quick_picks = int(input("How many quick picks? "))

    # Generate the quick picks
    quick_picks = [generate_quick_pick() for _ in range(num_quick_picks)]

    # Display the quick picks
    display_quick_picks(quick_picks)

if __name__ == "__main__":
    main()
