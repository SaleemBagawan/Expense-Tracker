from expense import *
from utils import validate_date
from datetime import datetime
import json

class ExpenseManager:

    def __init__(self):
        self.expenses= []
        self.next_id = 1
    
    def add_expense(self,date,amount, category,paid_by,payment_mode):
        if amount <=0 :
            raise ValueError('Invalid amount')
        if not category:
            raise ValueError('Category can not be empty.')
        if not paid_by:
            raise ValueError('paid_by can not be empty')
        if not payment_mode:
            raise ValueError('Mode can not be empty.')
        date = validate_date(date)
        if not date:
            raise ValueError('Invalid date')
        
        expense_id = self.next_id
        expense = Expense(expense_id,date,amount, category,paid_by,payment_mode)
        
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
    
    def get_total(self,filter_type = None, value = None):
        if not filter_type:
            return self.calculate_total(self.expenses)
        if not value:
                raise ValueError('Invalid input')
        if filter_type == 'category':
            return self.calculate_total(self.get_expenses_by_category(value.lower()))
        elif filter_type == 'paid_by':
            return self.calculate_total(self.get_expenses_by_paid_by(value.lower()))
        elif filter_type == 'payment_mode':
            return self.calculate_total(self.get_expenses_by_payment_mode(value.lower()))
        elif filter_type == 'date_range':
            return self.calculate_total(self.get_expenses_by_date_range(value[0],value[1]))
        else:
            raise ValueError('Invalid filter')
            

    def get_expenses_by_category(self,category):
        data = [c for c in self.expenses if c.category == category]
        return data
    
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
    
    def edit_expense(self, expense_id , amount = None , category = None , date = None , paid_by = None, payment_mode = None):

        expense = self.get_expense_by_id(expense_id)

        if expense is None:
            return False, 'Invalid ID'
        
        if amount is None and category is None and date is None and paid_by is None and payment_mode is None:
            return False, 'No changes Provided.'
        

        if amount is not None:
            if amount <=0 :
                raise ValueError('Invalid amount')
            expense.amount = amount
            
        if category is not None:
            if not category:
                raise ValueError('Category can not be empty.')
            expense.category = category

        if date is not None:
            date = validate_date(date)
            if not date:
                raise ValueError('Invalid date')
            expense.date = date

        if paid_by is not None:
            if not paid_by:
                raise ValueError('paid_by can not be empty')
            expense.paid_by = paid_by
        if payment_mode is not None:
            if not payment_mode:
                raise ValueError('Mode can not be empty.')
            expense.payment_mode = payment_mode

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
                self.expenses=[Expense.from_dict(self.validate_data(item)) for item in data]
        except FileNotFoundError:
            self.expenses = []

        if self.expenses:
            self.next_id = max(expense.expense_id for expense in self.expenses) + 1
        
    def validate_data(self,item):
        if not item.get('date',0):
            item['date'] = "01-10-0001"
        if not item.get('paid_by',0):
            item['paid_by'] = "Unknown"
        if not item.get('payment_mode',0):
            item['payment_mode'] = "Unknown"
        
        return item
    
    def get_expenses_by_date_range(self,start_date,end_date):
        start_date = validate_date(start_date)
        if not start_date:
            raise ValueError('Invalid date')
        end_date = validate_date(end_date)
        if not end_date:
            raise ValueError('Invalid date')
        start_date = datetime.strptime(start_date, "%d-%m-%Y")
        end_date = datetime.strptime(end_date, "%d-%m-%Y")
        if start_date > end_date:
            raise ValueError('Invalid date range')
        data = []
        for expense in self.expenses:
            expense_date = datetime.strptime(expense.date, "%d-%m-%Y")
            if start_date <= expense_date <= end_date:
                data.append(expense)
        return data
    
    def get_expenses_by_paid_by(self,paid_by):
        if not paid_by:
            raise ValueError('Invalid user')
        data = [c for c in self.expenses if c.paid_by == paid_by]
        return data
    
    def get_expenses_by_payment_mode(self,payment_mode):
        if not payment_mode:
            raise ValueError('Invalid payment mode.')
        data = [c for c in self.expenses if c.payment_mode == payment_mode]
        return data
        



        
    
       
        
    




    