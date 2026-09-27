from analyzer import BudgetAnalyzer

def main():
    app = BudgetAnalyzer()
    print("Welcome to the Expense Analyzer!")
    username = input("Enter your username: ")
    
    if username not in app.users:
        limit = float(input("Enter your monthly budget limit: ₹"))
        app.login(username, limit)
    else:
        app.login(username)
        
    while True:
        print("\n1. Add Expense\n2. View Analytics\n3. Exit")
        choice = input("Select an option: ")
        
        if choice == '1':
            try:
                amount = float(input("Amount: ₹"))
                category = input("Category (e.g., Food, Transport, Academics): ")
                desc = input("Description: ")
                app.record_expense(amount, category, desc)
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        elif choice == '2':
            app.generate_report()
        elif choice == '3':
            print("Saving data and exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()