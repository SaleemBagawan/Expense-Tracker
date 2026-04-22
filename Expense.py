class Expense:
   
    def __init__(self,expense_id,amount,category):
        self.expense_id = expense_id
        self.amount = amount
        self.category = category

    def to_dict(self):
        return {
            "expense_id":self.expense_id,
            "amount":self.amount,
            "category":self.category
        }
    
    @staticmethod
    def from_dict(data):
        return Expense(data['expense_id'],data['amount'],data['category'])
    




      


    
    