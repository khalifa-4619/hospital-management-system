from pydantic import BaseModel
from typing import Optional

class PatientBase(BaseModel):
    name: str
    age: int
    gender: str
    phone: Optional[str] = None
    
class PatienceCreate(PatientBase):
    pass

class patienceResponse(PatientBase):
    id: int
    
    class Config:
        from_attributes = True