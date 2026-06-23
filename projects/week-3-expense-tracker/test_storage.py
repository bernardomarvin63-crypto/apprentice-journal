from storage import load_expenses, save_expenses

# Try loading first - should be empty since no file exists yet
expenses = load_expenses()
print("Loaded: ", expenses)

# Add a fake expense and save
expenses.append({"amount": 250, "category": "groceries"})
expenses.append({"amount": 1500, "category": "fuel"})
save_expenses(expenses)
print("Saved 2 expenses.")

# Load again - now it should havae the data
expenses = load_expenses()
print("Loaded again:", expenses)