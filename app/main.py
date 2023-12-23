# app/main.py
from fastapi import FastAPI
from .routers import items, users

app = FastAPI()

# Include the item and user routers
print('leonardo')
app.include_router(items.router, prefix="/items", tags=["items"])
app.include_router(users.router, prefix="/users", tags=["users"])
