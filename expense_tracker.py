FILE_NAME = "expenses.txt"


def add_expense():
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))

    with open(FILE_NAME, "a") as file:
        file.write(f"{category},{amount}\n")

    print("Expense added successfully.")


def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

        if not records:
            print("No expenses recorded.")
            return

        total = 0

        print("\nExpense Report")
        print("--------------")

        for record in records:
            category, amount = record.strip().split(",")

            amount = float(amount)
            total += amount

            print(f"{category}: ₹{amount:.2f}")

        print("----------------")
        print(f"Total: ₹{total:.2f}")

    except FileNotFoundError:
        print("No expenses recorded.")


while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        break

    else:
        print("Invalid choice.")