from pydantic import BaseModel

class ApplicantBase(BaseModel):
    name: str
    email: str
    phone: str
    role: str
    status: str
    candidate_response: str

class ApplicantCreate(ApplicantBase):
    pass

class ApplicantResponse(ApplicantBase):
    id: int

    class Config:
        from_attributes = True   