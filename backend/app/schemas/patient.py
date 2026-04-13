from pydantic import BaseModel, Field
from typing import Optional

class PatientBase(BaseModel):
    name: str
    age: int = Field(gt=0)
    gender: str
    phone: Optional[str] = None
    
class PatientCreate(PatientBase):
    pass

class PatientResponse(PatientBase):
    id: int
    
    class Config:
        from_attributes = True