class Expense:
   
    def __init__(self,amount,category):
        self.amount = amount
        self.category = category

    def to_dict(self):
        return {
            "amount":self.amount,
            "category":self.category
        }
    
    @staticmethod
    def from_dict(data):
        return Expense(data['amount'],data['category'])
    
    
        
    



      


    
    