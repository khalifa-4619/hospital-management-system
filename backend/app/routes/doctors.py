from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.db import models
from app.schemas.doctor import DoctorCreate, DoctorResponse

router = APIRouter(prefix="/doctors", tags=["Doctors"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=DoctorResponse, status_code=201)
def create_doctor(doctor: DoctorCreate, db: Session = Depends(get_db)):
    new_doctor = models.Doctor(
        name=doctor.name,
        specialization=doctor.specialization,
        phone=doctor.phone,
        email=doctor.email
    )

    try:
        db.add(new_doctor)
        db.commit()
        db.refresh(new_doctor)
    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error creating doctor")
    
    return new_doctor


@router.get("/", response_model=list[DoctorResponse], status_code=200)
def get_doctors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    doctors = db.query(models.Doctor).offset(skip).limit(limit).all()
    return doctors