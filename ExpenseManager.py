from Expense import *
import json

class ExpenseManager:

    def __init__(self):
        self.expenses= []
        self.next_id = 1
    
    def add_expense(self,amount, category):
        if amount <=0 :
            raise ValueError('Invalid amount')
        if not category:
            raise ValueError('Category can not be empty.')
        
        expense_id = self.next_id
        expense = Expense(expense_id,amount, category)
        
        self.expenses.append(expense)
        self.next_id += 1
        self.save_to_file()

    def get_all_expenses(self):
        datalist = self.expenses.copy()
        return datalist
        
    def calculate_total(self,data):
        total = 0
        for expense in data:
            total += expense.amount
        return total
    
    def get_expenses_above_limit(self,limit):
        return [e for e in self.expenses if e.amount >= limit]
    
    def get_total(self):
        return self.calculate_total(self.expenses)
    
    def get_total_by_category(self,category):
        data = [c for c in self.expenses if c.category == category]
        return self.calculate_total(data)
    
    def get_expense_by_id(self,expense_id):
        for expense in self.expenses:
            if expense.expense_id == expense_id:
                return expense
        return None
    
    def delete_by_id(self,expense_id):
        expense = self.get_expense_by_id(expense_id)
        if expense is not None:
            self.expenses.remove(expense)
            self.save_to_file()
            return True
        return False
    
    def edit_expense(self, expense_id , amount = None , category = None):

        expense = self.get_expense_by_id(expense_id)

        if expense is None:
            return False, 'Invalid ID'
        
        if amount is None and category is None:
            return False, 'No changes Provided.'
        

        if amount is not None:
            if amount <=0 :
                raise ValueError('Invalid amount')
            expense.amount = amount
            
        if category is not None:
            if not category:
                raise ValueError('Category can not be empty.')
            expense.category = category

        self.save_to_file()

        return True , 'Expense updated successfully.'
    
    def save_to_file(self,filename='expenses.json'):
        data = [expense.to_dict() for expense in self.expenses]

        with open(filename,'w') as f:
            json.dump(data,f,indent=4)
        
    def load_from_file(self,filename='expenses.json'):
        try :
            with open(filename,'r') as f:
                data=json.load(f)
                self.expenses=[Expense.from_dict(item) for item in data]
        except FileNotFoundError:
            self.expenses = []

        if self.expenses:
            self.next_id = max(expense.expense_id for expense in self.expenses) + 1
        
    
       
        
    




    