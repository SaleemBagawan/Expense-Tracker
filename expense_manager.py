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

    def get_expenses(self, filter_by = None,filter_value = None,sort_by = None, order= None):
        data = self.expenses.copy()
        if filter_by:

            data = self.get_filtered_expenses(filter_by,filter_value,data)
        
        if sort_by:
            data = self.get_sorted_expenses(sort_by,data,order)

        return data
    
    def get_filtered_expenses(self,filter_by,filter_value,data):

        if filter_by == 'category':
            return self.get_expenses_by_category(filter_value.lower(),data)
        elif filter_by == 'paid_by':
            return self.get_expenses_by_paid_by(filter_value.lower(),data)
        elif filter_by == 'payment_mode':
            return self.get_expenses_by_payment_mode(filter_value.lower(),data)
        elif filter_by == 'date_range':
            return self.get_expenses_by_date_range(filter_value[0],filter_value[1],data)
        elif filter_by == 'above_limit':
            return self.get_expenses_above_limit(filter_value,data)
        else:
            raise ValueError('Invalid filter')
        
    def calculate_total(self,data):
        total = 0
        for expense in data:
            total += expense.amount
        return total
    
    def get_expenses_above_limit(self,limit,data = None):
        if data is not None:
            return [e for e in data if e.amount >= limit]
        else:
            return [e for e in self.expenses if e.amount >= limit]
    
    def get_total(self,filter_type = None, value = None):
        if not filter_type:
            return self.calculate_total(self.expenses)
        if not value:
                raise ValueError('Invalid input')
        if filter_type not in ['category','paid_by','payment_mode','date_range','above_limit']:
            raise ValueError('Invalid filter')
        if filter_type in ['category','paid_by','payment_mode']:
            value = value.lower()
        return self.calculate_total(self.get_expenses(filter_by=filter_type,filter_value=value))
            

    def get_expenses_by_category(self,category,data=None):
        if data is not None:
            return [c for c in data if c.category == category]
        else:
            return [c for c in self.expenses if c.category == category]
        
    
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
    
    def get_expenses_by_date_range(self,start_date,end_date,data = None):
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
        datalist=[]
        if data is not None:
            for expense in data:
                expense_date = datetime.strptime(expense.date, "%d-%m-%Y")
                if start_date <= expense_date <= end_date:
                    datalist.append(expense)
        else:
            for expense in self.expenses:
                expense_date = datetime.strptime(expense.date, "%d-%m-%Y")
                if start_date <= expense_date <= end_date:
                    datalist.append(expense)

        return datalist
    
    def get_expenses_by_paid_by(self,paid_by,data = None):
        if not paid_by:
            raise ValueError('Invalid user')
        if data is not None:
            return [c for c in data if c.paid_by == paid_by]
        else:
            return [c for c in self.expenses if c.paid_by == paid_by]

        
    
    def get_expenses_by_payment_mode(self,payment_mode,data = None):
        if not payment_mode:
            raise ValueError('Invalid payment mode.')
        if data is not None:
            return [c for c in data if c.payment_mode == payment_mode]
        else:
            return [c for c in self.expenses if c.payment_mode == payment_mode]

        
    
    def get_sorted_expenses(self, sort_by,data = None, order = 'asc'):

        if order not in ['asc','desc']:
            raise ValueError('Invalid order')
        if order is None:
            order = 'asc'

        reverse = True if order == 'desc' else False
        sort_by = sort_by.lower().strip()

        if sort_by not in ['category','amount' ,'date']:
            raise ValueError('invalid entry.')
        
        if sort_by == 'category':
            key = lambda expense:expense.category.lower()
        elif sort_by == 'amount':
            key = lambda expense:expense.amount
        elif sort_by == 'date':
            key = lambda expense:datetime.strptime(expense.date,"%d-%m-%Y")

        if data is not None:
            return sorted(data, key = key, reverse= reverse)
        else:
            return sorted(self.expenses , key = key , reverse=reverse)
    




        
    
       
        
    




    