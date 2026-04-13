from fastapi import FastAPI
from app.db.database import engine, Base
from app.db import models
from app.routes import patients


app = FastAPI()

app.include_router(patients.router, prefix="/patients", tags=["Patients"])

# Create tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Hospital management System API running"}