from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.models.item import Item
from pydantic import ValidationError

router = APIRouter()

@router.get("/")
def read_items():
    return {"message": "Read items"}

@router.post("/")
async def create_item(item: Item):
    try:
        return JSONResponse(content={"message": "item created succesfully", "item": item.dict()}, status_code= 201)
    
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
