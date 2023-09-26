def get_valid_score():
    while True:
        try:
            score = int(input("Enter a valid score (0-100 inclusive): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid input. Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid integer score.")


def print_result(score):
    if 90 <= score <= 100:
        result = "Excellent"
    elif 70 <= score < 90:
        result = "Good"
    elif 50 <= score < 70:
        result = "Pass"
    else:
        result = "Fail"

    print(f"Result: {result}")


def show_stars(score):
    print("*" * score)


def main():
    print("Welcome to the Score Program!")

    while True:
        print("\nMenu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input("Choose an option: ").strip().lower()

        if choice == 'g':
            score = get_valid_score()
        elif choice == 'p':
            if 'score' not in locals():
                print("Please enter a valid score first.")
            else:
                print_result(score)
        elif choice == 's':
            if 'score' not in locals():
                print("Please enter a valid score first.")
            else:
                show_stars(score)
        elif choice == 'q':
            print("Farewell! Thanks for using the Score Program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
