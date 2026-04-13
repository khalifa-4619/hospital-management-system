from pydantic import BaseModel
from datetime import datetime


class AppointmentBase(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_time: datetime


class AppointmentCreate(AppointmentBase):
    pass


class AppointmentResponse(AppointmentBase):
    id: int
    status: str

    class Config:
        from_attributes = True