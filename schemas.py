from pydantic import BaseModel
from datetime import date

class CertificateOut(BaseModel):
    certificate_id: str
    name: str
    college: str
    domain: str
    duration: str
    issue_date: date

    class Config:
        orm_mode = True
