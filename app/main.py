from fastapi import FastAPI
from .configs.database import engine, Base

app = FastAPI()

# Initialize database
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to HRX-SYNC!"}
