from sqlalchemy import Column, String, Integer, Date
from database import Base

class Certificate(Base):
    __tablename__ = "certificates"

    id = Column(Integer, primary_key=True, index=True)
    certificate_id = Column(String(100), unique=True, index=True, nullable=False)
    name = Column(String(100))
    college = Column(String(150))
    domain = Column(String(100))
    duration = Column(String(50))
    issue_date = Column(Date)
