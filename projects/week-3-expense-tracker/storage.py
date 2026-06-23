import json
import os

DATA_FILE = "data.json"

def load_expenses():
    # Read the list of expenses from disk. Return an empty list if no file exists yet.
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)
    
def save_expenses(expenses):
    # Write the list of expenses to disk as JSON.
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=2)