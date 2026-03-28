class Expense :

    def __init__(self,expense_id,date,amount,reason,paid_by):
        self.date = date
        self.expense_id = expense_id
        self.amount = amount
        self.reason = reason
        self.paid_by = paid_by

    def display(self):
        print("Date : ",self.date)
        print("Expense ID : ",self.expense_id)
        print("Amount : ",self.amount)
        print("Reason : ",self.reason)
        print("Paid by : ",self.paid_by)
        print("-" * 20)



