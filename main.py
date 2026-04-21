from ExpenseManager import *
from utils import *


def main():

    manager = ExpenseManager()
    
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
Please select the operation (1/2/3/4/5/6) :"""))
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
            for index in range(len(data)):
                print(f'{index} --> Amount : {data[index].amount} | Category : {data[index].category}')
        elif choice == 3:
            print(f'Total = {manager.get_total()}')
        elif choice == 4:
            limit = get_int_input('Enter the limit:')
            data = manager.get_expenses_above_limit(limit)
            if not data:
                print('No data found')
                continue
            for index in range(len(data)):
                print(f'{index} --> Amount : {data[index].amount} | Category : {data[index].category}')
        elif choice == 5:
            category = get_string_input('Enter the Category: ')
            data = manager.get_expenses_by_category(category)
            print(f'The Total amount for category {category} is {data}')
        elif choice == 6:
            index = get_int_input('Enter the index of the expense :')
            if not manager.delet_by_index(index):
                print('Index does not exists.')
            else:
                print('Expense deleted successfully.')
        elif choice == 7:
            data = {}
            index = get_int_input('Enter the index of expense : ')
            data['index'] = index
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
            
            if option == 1:
                amount = get_int_input('Enter the new amount :')
                status, massage = manager.edit_expense(index,amount = amount)
                print(f'{status} : {massage}')
            elif option == 2:
                category = get_string_input('Enter new category : ')
                status, massage = manager.edit_expense(index,category=category)
                print(f'{status} : {massage}')
                
            elif option == 3:
                amount = get_int_input('Enter the new amount :')
                category = get_string_input('Enter new category : ')
                status, massage = manager.edit_expense(index,amount = amount,category = category)
                print(f'{status} : {massage}')

            else:
                print('Invalid option')       
        else:
            break 

if __name__ == "__main__":
    main()
