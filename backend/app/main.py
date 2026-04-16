from fastapi import FastAPI
from app.db.database import engine, Base
from app.db import models
from app.routes import patients
from app.routes import appointments


app = FastAPI()

app.include_router(patients.router, prefix="/patients", tags=["Patients"])
app.include_router(appointments.router, prefix="/appointments", tags=["Appointments"])

# Create tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Hospital management System API running"}