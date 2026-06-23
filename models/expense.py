from sqlalchemy import Column, Integer,Float,String
from database import Base



class Expense(Base):

    __tablename__ = "expenses"

    expense_id = Column(Integer, primary_key = True, autoincrement = True)
    date = Column(String , nullable = False)
    amount = Column(Float ,nullable = False)
    category = Column(String , nullable = False)
    paid_by = Column(String, nullable = False)
    payment_mode = Column(String , nullable = False)
   
    



      


    
    