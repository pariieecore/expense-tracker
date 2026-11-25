import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

# Categories
CATEGORIES = ["Food", "Travel", "Study", "Bills", "Fun", "Other"]


# Create CSV file if it does not exist
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])


# Load expenses from CSV
def load_expenses():
    create_file()

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


# Save an expense to CSV
def save_expense(expense):
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["Date", "Category", "Description", "Amount"]
        )
        writer.writerow(expense)


# Validate date
def read_date():
    while True:
        date = input("Enter date (YYYY-MM-DD): ")

        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            print("Invalid date! Use YYYY-MM-DD format.")


# Validate amount
def read_amount():
    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
            else:
                return amount

        except ValueError:
            print("Please enter a valid amount.")


# Add expense
def add_expense():
    date = read_date()

    print("Categories:", ", ".join(CATEGORIES))
    category = input("Enter category: ").title()

    if category not in CATEGORIES:
        print("Invalid category!")
        return

    description = input("Enter description: ")
    amount = read_amount()

    expense = {
        "Date": date,
        "Category": category,
        "Description": description,
        "Amount": amount
    }

    save_expense(expense)
    print("Expense added successfully!")


# Display expenses
def display_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\nDate         Category      Description        Amount")
    print("-" * 60)

    for expense in expenses:
        print(
            f"{expense['Date']:<13}"
            f"{expense['Category']:<14}"
            f"{expense['Description']:<20}"
            f"₹{float(expense['Amount']):.2f}"
        )


# View all expenses
def view_expenses():
    expenses = load_expenses()
    display_expenses(expenses)


# Filter expenses
def filter_expenses():
    expenses = load_expenses()

    print("\n1. Filter by Category")
    print("2. Filter by Month")

    choice = input("Enter choice: ")

    if choice == "1":
        category = input("Enter category: ").title()

        filtered = [
            expense for expense in expenses
            if expense["Category"] == category
        ]

    elif choice == "2":
        month = input("Enter month (YYYY-MM): ")

        try:
            datetime.strptime(month, "%Y-%m")

            filtered = [
                expense for expense in expenses
                if expense["Date"][:7] == month
            ]

        except ValueError:
            print("Invalid month format!")
            return

    else:
        print("Invalid choice!")
        return

    display_expenses(filtered)


# Category summary
def summary():
    expenses = load_expenses()

    if not expenses:
        print("No expenses available.")
        return

    totals = {}
    grand_total = 0
    biggest_expense = expenses[0]

    for expense in expenses:
        category = expense["Category"]
        amount = float(expense["Amount"])

        totals[category] = totals.get(category, 0) + amount
        grand_total += amount

        if amount > float(biggest_expense["Amount"]):
            biggest_expense = expense

    print("\n--- Category Summary ---")

    for category, total in totals.items():
        print(f"{category}: ₹{total:.2f}")

    print(f"\nGrand Total: ₹{grand_total:.2f}")

    print(
        "Biggest Expense:",
        biggest_expense["Description"],
        f"(₹{float(biggest_expense['Amount']):.2f})"
    )


# Main menu
def main():
    create_file()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter Expenses")
        print("4. Category Summary")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            filter_expenses()

        elif choice == "4":
            summary()

        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
