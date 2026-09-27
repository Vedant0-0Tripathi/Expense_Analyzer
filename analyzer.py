import json
import os
from user import User
from expense import Expense

class BudgetAnalyzer:
    def __init__(self, filename="data.json"):
        self.filename = filename
        self.users = self.load_data()
        self.current_user = None

    def load_data(self):
        if not os.path.exists(self.filename):
            return {}
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                return {uname: User.from_dict(udata) for uname, udata in data.items()}
        except json.JSONDecodeError:
            return {}

    def save_data(self):
        with open(self.filename, "w") as f:
            json.dump({uname: user.to_dict() for uname, user in self.users.items()}, f, indent=4)

    def login(self, username, budget_limit=0.0):
        if username not in self.users:
            self.users[username] = User(username, budget_limit)
            self.save_data()
        self.current_user = self.users[username]

    def record_expense(self, amount, category, description):
        expense = Expense(amount, category, description)
        self.current_user.add_expense(expense)
        self.save_data()
        print(f"\nExpense added! ${amount:.2f} for {category}.")

    def generate_report(self):
        print(f"\n--- Analytics for {self.current_user.username} ---")
        total = self.current_user.total_spent()
        limit = self.current_user.budget_limit
        print(f"Total Budget: ${limit:.2f}")
        print(f"Total Spent:  ${total:.2f}")
        print(f"Remaining:    ${(limit - total):.2f}\n")
        
        categories = {}
        for exp in self.current_user.expenses:
            categories[exp.category] = categories.get(exp.category, 0) + exp.amount
            
        print("Spending by Category:")
        for cat, amt in categories.items():
            bar = "█" * int((amt / total) * 20) if total > 0 else ""
            print(f"{cat.ljust(12)} | ${amt:<6.2f} | {bar}")