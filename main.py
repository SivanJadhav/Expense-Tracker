from get import get_int, get_string
from file_io import load_json, save_json

options = """
Welcome to Expense Tracker
1. Add Expense
2. View Expenses
3. View Total by Category
4. Remove Expense
5. Exit
"""

# The name of the file in which we'll store the data
FILE_NAME = "expenses.json"

# Dictionary Format: {amount: int, category: str, date: DD/MM/YYYY str}
expenses: list

def main():

    # Load JSON Data into Expenses from file
    expenses = load_json(FILE_NAME)

    while True:

        # Print the options
        print(options)

        # Take user input
        response = get_int("Choose option: ", 1)

        # If input is equal to 1
        if response == 1:
            add_expense(expenses)

        # If input is equal to 2
        elif response == 2:
            # Print all expenses in the format: Price - Category - Date
            print_expenses(expenses)

        # If input is equal to 3
        elif response == 3:
            view_expenses_per_category(expenses)

        # If input is equal to 4
        elif response == 4:
            remove_expense(expenses)
            save_json(FILE_NAME, expenses, indent=4)

        # If input is equal to 5
        elif response == 5:
            # Exit the program (by using break)
            save_json(FILE_NAME, expenses, indent=4)
            break

def add_expense(expenses):
    # Ask amount
    amount = get_int("Enter amount: $", 1)

    # Ask for category
    category = get_string("Enter category: ")

    # Ask for date in DD/MM/YYYY form
    date = get_string("Enter date (in DD/MM/YYYY): ")
    day, month, year = 00, 00, 0000

    try:
        day, month, year = date.split("/")

    except:
        print("Invalid input.")

    # Save data to file
    try:
        expenses.append({
            "amount": amount,
            "category": category,
            "day": int(day),
            "month": int(month),
            "year": int(year)
        })

    except TypeError:
        print("Only integer values are accepted.")

    return_value = save_json(FILE_NAME, expenses, indent=4)

    # Give confirmation if added
    if return_value == 0:
        print("Expense added!")

def view_expenses_per_category(expenses):
    # Print total amount spent per category
    price_per_category = {}

    for expense in expenses:
        if expense["category"] not in price_per_category.keys():
            price_per_category[expense["category"]] = expense["amount"]

    print("Category Totals:")

    for category, expense in price_per_category.items():
        print(f"{category} - {expense}")

def remove_expense(expenses):
    # Take index as input and remove the task at that index
    print_expenses(expenses)

    # Take input on what to pop
    pop_index = get_int("Which expense do you want to remove? ", index=0)

    # Pop that index
    expenses.pop(pop_index)

def print_expenses(expenses):

    total_amount = 0

    for index, expense in enumerate(expenses, start=1):
        total_amount += expense["amount"]
        date = f"{expense["day"]:02d}/{expense["month"]:02d}/{expense["year"]:04d}"
        print(f"{index}. ${expense["amount"]} - {expense["category"]} - {date}")

    print(f"Total Amount Spent: ${total_amount}")

main()
