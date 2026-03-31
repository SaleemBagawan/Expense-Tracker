from models.expense import Expense
from services.tracker import ExpenseTracker
from utils.input_helper import *
import display 


traker = ExpenseTracker()

while True:
    try:
        print("-" * 30)
        action = int(input("""Select operation :
        1. Add expense
        2. Display expenses
        3. Exit
        Enter choice : """))
        print("-" * 30)
    except ValueError:
        print('Please Enter the Number of you choise :')
        continue
    if action == 1:
        expense_id = get_int_input('Enter the Expense ID : ')
        date = get_string_input('Enter Date :')
        amount = get_int_input('Enter the Amount : ')
        reason = get_string_input('State the reason : ')
        paid_by = get_string_input('Who paid? : ')

        expense = Expense(expense_id,date,amount,reason,paid_by)

        traker.add_expense(expense)

        print('Expense added successfully.')


    elif action == 2:
        trackr.display_expenses()

    else:
        break
    