from fastapi import APIRouter , HTTPException
from dependencies import manager
from schemas.expense import ExpenseCreate, ExpenseResponse , ExpenseUpdate

router = APIRouter()


@router.post("/expenses",status_code=201)
def add_expense(expense:ExpenseCreate):
    try:
        manager.add_expense(expense.date,expense.amount,expense.category.lower(),expense.paid_by.lower(),expense.payment_mode.lower())
        return {"message": "Expense added successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/expenses")
def get_expenses(filter_by:str=None, filter_value:str=None, sort_by:str=None, order:str=None, start_date: str=None, end_date:str=None):
    if filter_by == "date_range":
        filter_value = (start_date,end_date)
    if filter_by == "above_limit":
        try:
            filter_value = int(filter_value)
        except ValueError:
            raise HTTPException(status_code=400, detail="above_limit filter requires a valid number")
    try:
        return [expense.to_dict() for expense in manager.get_expenses(filter_by,filter_value,sort_by,order)]
        
    except ValueError as e:
        raise HTTPException(status_code=400,detail=str(e))
    
@router.put("/expenses/{expense_id}")
def edit_expense(expense_id:int, updated_expense :ExpenseUpdate):
    try :
        status , message = manager.edit_expense(expense_id,updated_expense.amount,updated_expense.category.lower(),updated_expense.date,updated_expense.paid_by.lower(),updated_expense.payment_mode.lower())
        if status:
            return {"message" : "Expense updated successfully"}
        else:
            return {"message" : message}
    except ValueError as e:
        raise HTTPException(status_code=400,detail=str(e))

@router.delete("/expenses/{expense_id}")
def delete_expense(expense_id:int):
    try:
        if manager.delete_by_id(expense_id):
            return {"message" : "expense deleted"}
        else:
            raise HTTPException(status_code=404, detail='Expense not found')
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@router.get("/expenses/total")
def get_total(filter_type : str= None, value : str = None, start_date : int= None, end_date : str = None):
    if filter_type == "date_range":
        value = (start_date,end_date)
    if filter_type == "above_limit":
        try:
            value = int(value)
        except ValueError:
            raise HTTPException(status_code=400, detail="above_limit filter requires a valid number")
    try:
        return manager.get_total(filter_type,value)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    


