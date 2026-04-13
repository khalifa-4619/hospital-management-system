from pydantic import BaseModel
from typing import Optional


class DoctorBase(BaseModel):
    name: str
    specialization: str
    phone: str
    email: Optional[str] = None


class DoctorCreate(DoctorBase):
    pass


class DoctorResponse(DoctorBase):
    id: int

    class Config:
        from_attributes = True