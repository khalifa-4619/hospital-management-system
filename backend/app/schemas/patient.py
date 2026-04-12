from pydantic import BaseModel
from typing import Optional

class PatientBase(BaseModel):
    name: str
    age: int
    gender: str
    phone: Optional[str] = None
    
class PatientCreate(PatientBase):
    pass

class patientResponse(PatientBase):
    id: int
    
    class Config:
        from_attributes = True