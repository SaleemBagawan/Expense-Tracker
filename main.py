from expense_manager import *
from utils import *


def main():

    manager = ExpenseManager()
    manager.load_from_file()

    while True:
        print('*' * 40)
        try:
            choice = int(input("""
1. Add expense
2. View Expenses
3. Edit expense
4. Delete Expense
5. Display Total
Please select the operation (1/2/3/4/5) :"""))
        except ValueError:
            print('Please enter valid operation:')
            continue
        
        print('*' * 40)

        if choice == 1:
            amount = get_int_input('Enter amount:')
            category = get_string_input('Enter Category : ')
            date = get_string_input('Enter date (dd-mm-yyyy):')
            paid_by = get_string_input('Who paid ? : ')
            payment_mode = get_string_input('Mode of payment :')
            try:
                manager.add_expense(date,amount, category.lower(),paid_by.lower(),payment_mode.lower())
                print('Expense added successfully')
                
            except ValueError as e:
                print(e)


        elif choice == 2:
            try:
                print('View Expenses')
                apply_filter = get_string_input('Apply Filter? (y/n):')
                if apply_filter == 'y':
                    choice = get_int_input("""
Filter by:
1. Category
2. User
3. Payment mode
4. Date range
5. Above limit
select (1/2/3/4/5)""")
                    if choice == 1:
                        filter_by = 'category'
                        filter_value = get_string_input("Enter category:")
                    elif choice == 2:
                        filter_by = 'paid_by'
                        filter_value = get_string_input('Enter user :')
                    elif choice == 3:
                        filter_by = 'payment_mode'
                        filter_value = get_string_input('Enter payment mode:')
                    elif choice == 4:
                        filter_by = 'date_range'
                        start_date = get_string_input('Enter start date:')
                        end_date = get_string_input('Enter end date:')
                        filter_value = (start_date,end_date)
                    elif choice == 5:
                        filter_by = 'above_limit'
                        filter_value = get_int_input('Enter limit')
                    else:
                        raise ValueError('Invalid input')
                elif apply_filter == 'n':
                    filter_by = None
                    filter_value  = None
                else:
                    raise ValueError('Invalid input')
                
                apply_sort = get_string_input('Apply Sort? (y/n):')
                if apply_sort == 'y':
                    option = int(input("""
Sort By:
    1. Amount
    2. Category
    3. Date
Enter selection (1/2/3): """))
                    if option == 1:
                        sort_by = 'amount'
                    elif option == 2:
                        sort_by = 'category'
                    elif option == 3:
                        sort_by = 'date'
                    else:
                        raise ValueError('Invalid input')

                    order = get_string_input('Order (asc/desc):')
                elif apply_sort == 'n':
                    sort_by = None
                    order = None
                else:
                    raise ValueError('Invalid input')
                

                data = manager.get_expenses(filter_by=filter_by,filter_value=filter_value,sort_by=sort_by,order=order)
                if not data:
                    print('No record found')
                    continue
                print_expense_tables(data)  
            except ValueError as e:
                print(e)
                continue
            



            
        elif choice == 3:
            expense_id = get_int_input('Enter the id of expense : ')
            try : 
                option = int(input("""
Edit options
    1. Edit amount
    2. Edit category
    3. Edit both amount and category
    4. Edit paid by
    5. Edit payment mode
    6. Edit date
Select option (1/2/3/4/5/6) : """))
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
                    status, message = manager.edit_expense(expense_id,category=category.lower())
                    print(message)
                    
                elif option == 3:
                    amount = get_int_input('Enter the new amount :')
                    category = get_string_input('Enter new category : ')
                    status, message = manager.edit_expense(expense_id,amount = amount,category = category.lower())
                    print(message)
                elif option == 4:
                    paid_by = get_string_input('Enter new paid by:')
                    status , message = manager.edit_expense(expense_id,paid_by=paid_by.lower())
                    print(message)
                elif option == 5:
                    payment_mode = get_string_input('Edit mode:')
                    status , message = manager.edit_expense(expense_id, payment_mode = payment_mode.lower())
                    print(message)
                elif option == 6:
                    date = get_string_input('Edit date:')
                    status, message = manager.edit_expense(expense_id, date = date)
                    print(message)
                else:
                    print('Error : Invalid option')
            except ValueError as e:
                print(e)


                

        elif choice == 4:
            expense_id = get_int_input('Enter the id of the expense :')
            if not manager.delete_by_id(expense_id):
                print('Id does not exists.')
            else:
                print('Expense deleted successfully.')



        elif choice == 5:
            try:
                option = int(input("""
Display Total
    1. Total of all
    2. Total by category
    3. Total by user
    4. Total by payment mode
    5. Total by date range
Enter option (1/2/3/4/5):"""))
            except ValueError:
                print('Invalid option')
                continue

            try:
                if option == 1:
                    print(f"Toatal of all expenses : {manager.get_total()}")
                elif option == 2:
                    category = get_string_input('Enter the Category: ')
                    print(f'The Total amount for category "{category}" is {manager.get_total(filter_type='category',value=category.strip())}')
                elif option == 3:
                    user = get_string_input('Enter user :')
                    print(f'The Total amount for user "{user}" is {manager.get_total(filter_type='paid_by',value=user.strip())}')
                elif option == 4:
                    payment_mode = get_string_input('Enter payment mode.')
                    print(f'The Total amount for Pyament mode "{payment_mode}" is {manager.get_total(filter_type='payment_mode',value=payment_mode.strip())}')
                elif option == 5:
                    start_date = get_string_input('Enter start date:')
                    end_date = get_string_input('Enter end date:')
                    print(f"Total from {start_date} to {end_date} is : {manager.get_total(filter_type='date_range',value=(start_date,end_date))}")
                else:
                    raise ValueError('invalid option')
            except ValueError as e:
                print(e)

        else:
            break 

if __name__ == "__main__":
    main()
