from Expense import *
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
        return self.calculate_total(self.get_all_expenses())
    
    def get_expenses_by_category(self,category):
        data = [c for c in self.expenses if c.category == category]
        return self.calculate_total(data)
    
    def delet_by_index(self,index):
        if 0 <= index <= len(self.expenses):
            del self.expenses[index]
            return True
        return False
    




    