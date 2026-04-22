from ExpenseManager import *
from utils import *


def main():

    manager = ExpenseManager()
    manager.load_from_file()

    while True:
        print('*' * 40)
        try:
            choice = int(input("""
1. Add expense
2. Display expenses
3. Display Total
4. Display above limit
5. Display total by category
6. Delete Expense 
7. Edit expense
8. Exit
Please select the operation (1/2/3/4/5/6/7/8) :"""))
        except ValueError:
            print('Please enter valid operation:')
            continue
        
        print('*' * 40)

        if choice == 1:
            amount = get_int_input('Enter amount:')
            category = get_string_input('Enter Category : ')
            try:
                manager.add_expense(amount, category)
                print('Expense added successfully')
                
            except ValueError as e:
                print(e)
        elif choice == 2:
            data = manager.get_all_expenses()
            if not data:
                print('No record found')
                continue
            for expense in data:
                print(f'{expense.expense_id} --> Amount : {expense.amount} | Category : {expense.category}')
        elif choice == 3:
            print(f'Total = {manager.get_total()}')
        elif choice == 4:
            limit = get_int_input('Enter the limit:')
            data = manager.get_expenses_above_limit(limit)
            if not data:
                print('No data found')
                continue
            for expense in data:
                print(f'{expense.expense_id} --> Amount : {expense.amount} | Category : {expense.category}')
        elif choice == 5:
            category = get_string_input('Enter the Category: ')
            data = manager.get_total_by_category(category)
            print(f'The Total amount for category {category} is {data}')
        elif choice == 6:
            expense_id = get_int_input('Enter the id of the expense :')
            if not manager.delete_by_id(expense_id):
                print('Id does not exists.')
            else:
                print('Expense deleted successfully.')
            
        elif choice == 7:
            expense_id = get_int_input('Enter the id of expense : ')
            try : 
                option = int(input("""
Edit options
1. Edit amount
2. Edit category
3. Edit both amount and catergory
Select option (1/2/3) : """))
            except ValueError:
                print('Invalid number:')
                continue
            try:
                if option == 1:
                    amount = get_int_input('Enter the new amount :')
                    status, message = manager.edit_expense(expense_id,amount = amount)
                    print(message)
                elif option == 2:
                    category = get_string_input('Enter new category : ')
                    status, message = manager.edit_expense(expense_id,category=category)
                    print(message)
                    
                elif option == 3:
                    amount = get_int_input('Enter the new amount :')
                    category = get_string_input('Enter new category : ')
                    status, message = manager.edit_expense(expense_id,amount = amount,category = category)
                    print(message)

                else:
                    print('Error : Invalid option')
            except ValueError as e:
                print(e)
        else:
            break 

if __name__ == "__main__":
    main()
