from expenses import add_expense, list_expenses, total_expenses

# Clear any old data by importing storage directly and saving an empty list
from storage import save_expenses
save_expenses([])
print("Cleared all expenses.\n")

# Add some sample expenses
add_expense(250, "groceries")
add_expense(1500, "fuel")
add_expense(80, "groceries")
add_expense(300, "transport")
print("Add 4 expenses.\n")

# List them all 
print("All expenses:")
for expense in list_expenses():
    print(f"{expense['date']} | PHP {expense['amount']:>6} | {expense['category']}")
print()

# Show totals
print(f"Total spent: PHP {total_expenses()}")
print(f"Groceries total: PHP {total_expenses(category='groceries')}")
print(f"Fuel total: PHP {total_expenses(category='fuel')}")