

def display_expense(expense):
    print("Date:", expense.date)
    print("Expense ID:", expense.expense_id)
    print("Amount:", expense.amount)
    print("Reason:", expense.reason)
    print("Paid by:", expense.paid_by)
    print("-" * 20)


def display_expenses(expenses):
    if not expenses:
        print("No expenses found")
        return
    
    for expense in expenses:
        display_expense(expense)



