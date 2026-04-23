
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

def print_expense_tables(data):
    print(f"{'ID':>5} | {'Date':<10} | {'Amount':<10} | {'Category':<20} | {'Paid By':<10} | {'Payment mode':<10}")
    widths = [5,10,10,20,10,10]
    total_width = sum(widths) + ((len(widths) -1) * 3)
    print('-' * total_width)
    for expense in data:
        print(f"{expense.expense_id:>5} | {expense.date:<10} | {expense.amount:>10} | {expense.category:<20} | {expense.paid_by:<10} | {expense.payment_mode:<10}")
    

def validate_date(date):
    from datetime import datetime 
    try:
        dt = datetime.strptime(date, "%d-%m-%Y")
        return dt.strftime("%d-%m-%Y")
    except ValueError:
        return False
