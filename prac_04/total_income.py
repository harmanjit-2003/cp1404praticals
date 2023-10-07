# def main():
#     """Display income report for incomes over a given number of months."""
#     incomes = []
#     number_of_months = int(input("How many months? "))
#
#     for month in range(1, number_of_months + 1):
#         income = float(input(f"Enter income for month {month}: "))
#         incomes.append(income)
#
#     print_report(incomes)
#
#
# def print_report(incomes):
#     """Print report based on incomes."""
#     # Note that we do not need to pass in number_of_months
#     # because we know the length of the incomes list
#     print("\nIncome Report\n-------------")
#     total = 0
#     for month, income in enumerate(incomes, 1):
#         total += income
#         print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")
#
#
# main()


def get_monthly_incomes():
    incomes = []
    months = int(input("How many months? "))
    for month in range(1, months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)
    return incomes

def print_income_report(incomes):
    print("\nIncome Report")
    print("-------------")
    total_income = 0
    for month, income in enumerate(incomes, start=1):
        total_income += income
        print(f"Month {month:2} - Income: ${income:8.2f} Total: ${total_income:8.2f}")

def main():
    incomes = get_monthly_incomes()
    print_income_report(incomes)

if __name__ == "__main__":
    main()
