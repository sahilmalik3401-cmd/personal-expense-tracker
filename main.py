import csv
import os

FILE_NAME = "expenses.csv"


def add_expense():
    amount = float(input("Enter amount (Rs): "))
    category = input("Enter category (Food/Travel/Bills): ")
    description = input("Enter description: ")

    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists or os.path.getsize(FILE_NAME) == 0:
            writer.writerow(["Amount", "Category", "Description"])

        writer.writerow([amount, category, description])

    print("Expense added successfully!")


def show_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    total = 0

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            print(row)
            total += float(row["Amount"])

    print("Total expenses: Rs", total)


def category_summary():
    totals = {}

    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])
            totals[category] = totals.get(category, 0) + amount

    print("\nCategory-wise expenses:")
    for category, amount in totals.items():
        print(category, ": Rs", amount)


while True:
    print("\n--- Personal Expense Tracker ---")
    print("1. Add Expense")
    print("2. Show All Expenses")
    print("3. Category Summary")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        category_summary()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Try again.")




        
