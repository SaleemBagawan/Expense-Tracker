class Expense:
    index = 1
    def __init__(self,amount,category):
        self.amount = amount
        self.category = category
        self.index = Expense.index

        Expense.index += 1
    



      


    
    