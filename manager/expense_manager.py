from models.expense import Expense
from utils import validate_date
from sqlalchemy import asc , desc , func


class ExpenseManager:

    
    
    def add_expense(self,db,date,amount, category,paid_by,payment_mode):
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
        
        
        expense = Expense(date=date,amount=amount, category=category,paid_by=paid_by,payment_mode=payment_mode)
        db.add(expense)
        db.commit()
        db.refresh(expense)
        

    def get_expenses(self,db, filter_by = None,filter_value = None,sort_by = None, order= None):
        query = db.query(Expense)
        if filter_by:
            if filter_by == 'date_range':
                start_date = validate_date(filter_value[0])
                end_date = validate_date(filter_value[1])
                query = query.filter(Expense.date >= start_date, Expense.date <= end_date)
            elif filter_by == 'above_limit':
                query = query.filter(Expense.amount >= filter_value)
            else:
                column = getattr(Expense , filter_by)
                query=query.filter(column == filter_value)
        
        if sort_by:
            if order is None:
                order = 'asc'
            if order not in ['asc','desc']:
                raise ValueError('Invalid order')
            if order == 'desc':
                query = query.order_by(desc(getattr(Expense , sort_by)))
            else:
                query = query.order_by(asc(getattr(Expense,sort_by)))

        return query.all()
    
   
    
    def get_expense_by_id(self,db,expense_id):
        return db.query(Expense).filter(Expense.expense_id == expense_id).first()
            
         
    
    def delete_by_id(self,db,expense_id):
        expense = self.get_expense_by_id(db,expense_id)
        if expense is not None:
            db.delete(expense)
            db.commit()
            return True
        return False
    
    def edit_expense(self,db, expense_id , amount = None , category = None , date = None , paid_by = None, payment_mode = None):

        expense = self.get_expense_by_id(db,expense_id)

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

        db.commit()

        return True , 'Expense updated successfully.'
    
    
    def get_total(self,db,filter_by = None, value = None):
        query = db.query(func.sum(Expense.amount))
        if filter_by:
            if filter_by == 'date_range':
                start_date = validate_date(value[0])
                end_date = validate_date(value[1])
                query = query.filter(Expense.date >= start_date, Expense.date <= end_date)
            elif filter_by == 'above_limit':
                query = query.filter(Expense.amount >= value)
            else:
                column = getattr(Expense , filter_by)
                query=query.filter(column == value)
        return query.scalar()
        
   
    
    
        
    
       
        
    




    