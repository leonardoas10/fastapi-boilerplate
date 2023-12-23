# main.py
from fastapi import FastAPI
from app.main import app as app_in_app

app = FastAPI()

# Include the entire FastAPI app from app/main.py
app.mount("/", app_in_app)
