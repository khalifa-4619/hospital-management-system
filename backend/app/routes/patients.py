from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.db import models
from app.schemas.patient import PatientCreate, PatientResponse

router = APIRouter(prefix="/patients", tags=["Patients"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=PatientResponse, status_code=201)
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    new_patient = models.Patient(
        name=patient.name,
        age=patient.age,
        gender=patient.gender,
        phone=patient.phone
    )

    try:
        db.add(new_patient)
        db.commit()
        db.refresh(new_patient)
    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error creating patient")

    return new_patient


@router.get("/", response_model=list[PatientResponse], status_code=200)
def get_patients(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    patients = db.query(models.Patient).offset(skip).limit(limit).all()
    return patients