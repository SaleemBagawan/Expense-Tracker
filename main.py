class Expense:

    def __init__(self,amount,category):
        self.amount = amount
        self.category = category

class ExpenseManager:

    def __init__(self):
        self.expenses= []
    
    def add_expense(self,amount, category):
        if amount <=0 :
            raise ValueError('Invalid amount')
        if not category:
            raise ValueError('Category can not be empty.')
        expense = Expense(amount, category)
        self.expenses.append(expense)

    def get_expenses(self):
        return self.expenses
        
    def calculate_total(self):
        total = 0
        for expense in self.expenses:
            total += expense.amount
        return total
    
    def display_above_limit(self,limit):
        return [e for e in self.expenses if e.amount >= limit]

    
    
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
            5. Exit
            Please select the operation (1/2/3/4/5) :"""))
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
            data = manager.get_expenses()
            if not data:
                print('No record found')
                continue
            for expense in data:
                print(f'Amount : {expense.amount}  Category : {expense.category}')

        
        elif choice == 3:
            print(f'Total = {manager.calculate_total()}')

        elif choice == 4:
            limit = get_int_input('Enter the limit:')
            data = manager.display_above_limit(limit)
            if not data:
                print('No data found')
                continue
            for entry in data:
                print(f'Amount : {entry.amount}  Category : {entry.category}')
            
            
        else:
            break
    



def get_int_input(text):
    while True:
        try:
            return int(input(text))
        except ValueError:
            print('Please enter a valid number.')

def get_string_input(text):
    while True:
        value = input(text)
        if not value:
            print('Please enter something:')
        else:
            return value
    

if __name__ == "__main__":
    main()
