from expense import Expense

class User:
    def __init__(self, username, budget_limit=0.0):
        self.username = username
        self.budget_limit = float(budget_limit)
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def total_spent(self):
        return sum(exp.amount for exp in self.expenses)

    def to_dict(self):
        return {
            "username": self.username,
            "budget_limit": self.budget_limit,
            "expenses": [exp.to_dict() for exp in self.expenses]
        }

    @classmethod
    def from_dict(cls, data):
        user = cls(data["username"], data["budget_limit"])
        for exp_data in data.get("expenses", []):
            user.add_expense(Expense(**exp_data))
        return user