# app/models/item.py
from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str = Field( description="The name of the item", min_length=1)
    description: str = None
