def main():
    name = input("Enter name: ")

    while True:
        print("(H)ello")
        print("(G)oodbye")
        print("(Q)uit")
        choice = input(">>> ").upper()

        if choice == 'Q':
            print("Finished.")
            break
        elif choice == 'H':
            print(f"Hello {name}")
        elif choice == 'G':
            print(f"Goodbye {name}")
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

