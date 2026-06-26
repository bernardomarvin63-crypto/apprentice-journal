from datetime import datetime
from storage import load_expenses, save_expenses

def add_expense(amount, category):
    # Add a new expense to storage. Returns the saved expense dict.
    expenses = load_expenses()
    new_expense = {
        "amount": amount,
        "category": category,
        "date": datetime.now().isoformat(timespec="seconds"),
    }
    expenses.append(new_expense)
    save_expenses(expenses)
    return new_expense

def list_expenses():
    # Return all expenses currently in storage.
    return load_expenses()

def total_expenses(category=None):
    # Return the total amount spent. If category is given, filter by it.
    expenses = load_expenses()
    if category is not None:
        expenses = [e for e in expenses if e["category"] == category]
    return sum(e["amount"] for e in expenses)