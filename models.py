from sqlalchemy import Column, Integer, String
from database import Base

class InternApplicant(Base):
    __tablename__ = "intern_applicants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100), unique=True)
    phone = Column(String(20))
    role = Column(String(50))
    status = Column(String(50))
    candidate_response = Column(String(255))