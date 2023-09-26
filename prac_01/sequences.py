def show_even_numbers(x, y):
    for num in range(x, y + 1):
        if num % 2 == 0:
            print(num, end=' ')
    print()

def show_odd_numbers(x, y):
    for num in range(x, y + 1):
        if num % 2 != 0:
            print(num, end=' ')
    print()

def show_squares(x, y):
    for num in range(x, y + 1):
        square = num * num
        print(square, end=' ')
    print()

def main():
    x = int(input("Enter the start number (x): "))
    y = int(input("Enter the end number (y): "))

    while True:
        print("\nMenu:")
        print("1. Show the even numbers from x to y")
        print("2. Show the odd numbers from x to y")
        print("3. Show the squares of the numbers from x to y")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            show_even_numbers(x, y)
        elif choice == '2':
            show_odd_numbers(x, y)
        elif choice == '3':
            show_squares(x, y)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
