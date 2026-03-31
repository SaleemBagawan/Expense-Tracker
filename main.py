expenses = []

def add_expense(amount,category):
    expense = {'amount':amount , 'category':category}
    expenses.append(expense)

def display_expenses():
    if not expenses:
        print("No expense found")
        return 
    for record in expenses:
        print(f"Amount : {record['amount']}  Category : {record['category']}")

def calculate_total():
    total = 0
    for record in expenses:
        total += record['amount']

    return total

def display_total(total):
    print(f"Total expense : {total}")

def display_expenses_above(limit):
    found = False
    for record in expenses:
        if record['amount'] >= limit:
            found = True
            print(f"Amount : {record['amount']}  Category : {record['category']}")

    if not found:
        print("No record found")
        
    


add_expense(100,'Grocery')
add_expense(120,'Food')
add_expense(170,'Electricity Bill')
add_expense(190,'Room rent')

display_expenses()
display_total(calculate_total())
display_expenses_above(500)

