from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.db import models
from app.schemas.patient import PatientCreate, patientResponse


router = APIRouter()

# Dependency (DB session)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# CREATE PATIENT
@router.post("/", response_model=patientResponse)
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    new_patient = models.Patient(
        name=patient.name,
        age=patient.age,
        gender=patient.gender,
        phone=patient.phone
    )
    
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    
    return new_patient


# GET ALL PATIENTS
@router.get("/", response_model=list[patientResponse])
def get_patients(db: Session = Depends(get_db)):
    patients = db.query(models.Patient).all()
    return patients