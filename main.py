from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
from database import SessionLocal, engine, Base

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# ✅ Default route
@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}

# ✅ Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ Certificate verification route
@app.get("/verify/{certificate_id}", response_model=schemas.CertificateOut)
def verify_certificate(certificate_id: str, db: Session = Depends(get_db)):
    cert = db.query(models.Certificate).filter(models.Certificate.certificate_id == certificate_id).first()
    if not cert:
        raise HTTPException(status_code=404, detail="Certificate not found")
    return cert
