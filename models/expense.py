class Expense:
   
    def __init__(self,expense_id,date,amount,category,paid_by,payment_mode):
        self.expense_id = expense_id
        self.amount = amount
        self.category = category
        self.date = date
        self.payment_mode = payment_mode
        self.paid_by = paid_by

    def to_dict(self):
        return {
            "expense_id":self.expense_id,
            "date":self.date,
            "amount":self.amount,
            "category":self.category,
            "paid_by":self.paid_by,
            "payment_mode":self.payment_mode
        }
    
    @staticmethod
    def from_dict(data):
        return Expense(data['expense_id'],data['date'],data['amount'],data['category'],data['paid_by'],data['payment_mode'])
    




      


    
    