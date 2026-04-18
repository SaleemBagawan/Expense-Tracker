

def add_expense(amount,category,expenses):
    expense = {'amount':amount , 'category':category}
    expenses.append(expense)


def display_expenses(expenses):
    if not expenses:
        print("No expense found")
        return 
    for record in expenses:
        print(f"Amount : {record['amount']}  Category : {record['category']}")

def calculate_total(expenses):
    total = 0
    for record in expenses:
        total += record['amount']

    return total


def display_expenses_above(limit,expenses):
    found = False
    for record in expenses:
        if record['amount'] >= limit:
            found = True
            print(f"Amount : {record['amount']}  Category : {record['category']}")

    if not found:
        print("No record found")
        
def get_int_input(text):
    while True:
        try:
            return int(input(text))
        except ValueError:
            print('please enter valid Number:')

def get_string_input(text):
    while True:
        data = input(text)
        if not data:
            print('Enter can not be empty, please enter valid entry')
        else:
            return data
    



def main ():
    expenses = []

    while True:
        print('*' * 20)
        print('Please select the Operation :')
        try:
            choice = int(input("""
            1) Add expense
            2) Display expenses
            3) Disply total
            4) Disply expense above the limit
            5) Exit
            Please enter the choice (1/2/3/4/5) : """))
        except ValueError:
            print("Please enter a valid choice:")
            continue
        print('*' * 20)

        if choice == 1:
            amount = get_int_input('Please enter the amount:')
            category = get_string_input('Please enter the category:')
            add_expense(amount,category,expenses)
            print('Expense added successfully:')
        elif choice == 2:
            display_expenses(expenses)
        elif choice == 3:
            print(f'Total expense = {calculate_total(expenses)}')
        elif choice == 4:
            limit = get_int_input('Enter the limit:')
            display_expenses_above(limit,expenses)
        else:
            break

main()



