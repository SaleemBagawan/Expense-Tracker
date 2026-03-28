class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self,expense):
        self.expenses.append(expense)

    def display_expenses(self):
        if not self.expenses:
            print('No expenses found')
            return
        for expense in self.expenses:
            expense.display()

            
