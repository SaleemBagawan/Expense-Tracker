from fastapi import FastAPI
from routers import expenses
from database import Base,engine
from fastapi.middleware.cors import CORSMiddleware


Base.metadata.create_all(bind = engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(expenses.router)
