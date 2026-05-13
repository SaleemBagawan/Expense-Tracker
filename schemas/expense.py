from pydantic  import BaseModel
from typing import Optional

class ExpenseCreate(BaseModel):
    amount : float
    category : str
    date : str
    payment_mode : str
    paid_by : str


class ExpenseResponse(ExpenseCreate):
    expense_id : int

    class Config:
        from_attributes = True

class ExpenseUpdate(BaseModel):
    amount: Optional[float] = None
    category: Optional[str] = None
    date: Optional[str] = None
    paid_by: Optional[str] = None
    payment_mode: Optional[str] = None

    
