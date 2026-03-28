from models.expense import Expense
from services.tracker import ExpenseTracker

traker = ExpenseTracker()

while True:
    print("-" * 30)
    action = int(input("""Select operation :
    1. Add expense
    2. Display expenses
    3. Exit
    Enter choice : """))
    print("-" * 30)
    if action == 1:
        expense_id = int(input('Enter Expense ID : '))
        date = input("Enter Date : ")
        amount = int(input('Enter the Amount : '))
        reason = input('State the reason : ')
        paid_by = input('Who paid? : ')

        expense = Expense(expense_id,date,amount,reason,paid_by)

        traker.add_expense(expense)

        print('Expense added successfully.')


    elif action == 2:
        traker.display_expenses()

    else:
        break
    