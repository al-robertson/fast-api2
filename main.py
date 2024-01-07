from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated
import models
import schemas
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy import func
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    #allow_origins=["http://localhost:3000","http://172.167.82.148:3000"], 
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/contacts", response_model=List[schemas.ContactResponse])
async def fetch_contacts(db: db_dependency):
    result = db.query(models.Contacts).all()
    if not result:
        raise HTTPException(status_code=404, detail='Contacts can''t be read.')
    return result

@app.post("/contacts")
async def create_contact(contact: schemas.ContactCreate, db: db_dependency):
    new_contact = models.Contacts(
        name=contact.name,
        email=contact.email,
        age=contact.age,
        phone=contact.phone,
        address=contact.address,
        city=contact.city,
        zipCode=contact.zipCode,
        registrarId=contact.registrarId
    )
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return new_contact

@app.put("/contacts_edit/{contact_id}")
async def update_contact(contact_id: int, contact: schemas.ContactCreate, db: db_dependency):
    existing_contact = db.query(models.Contacts).filter(models.Contacts.id == contact_id).first()
    if existing_contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")

    existing_contact.name = contact.name
    existing_contact.email = contact.email
    existing_contact.age = contact.age
    existing_contact.phone = contact.phone
    existing_contact.address = contact.address
    existing_contact.city = contact.city
    existing_contact.zipCode = contact.zipCode
    existing_contact.registrarId = contact.registrarId

    db.commit()
    #db.refresh(existing_contact)
    return existing_contact


@app.delete("/contacts_delete/{contact_id}")
async def delete_contact(contact_id: int, db: db_dependency):
    contact_to_delete = db.query(models.Contacts).filter(models.Contacts.id == contact_id).first()
    if contact_to_delete is None:
        raise HTTPException(status_code=404, detail="Contact not found")

    db.delete(contact_to_delete)
    db.commit()
    return {"detail": "Contact deleted successfully"}

@app.get("/countrysales")
async def fetch_country_sales(db: Session = Depends(get_db)):
    result = db.query(models.CountrySalesView).all()
    if not result:
        raise HTTPException(status_code=404, detail='Can''t get sales data')
    return result

@app.get("/transportrevenue")
async def fetch_transport_revenue(db: Session = Depends(get_db)):
    
    #get records
    result = db.query(models.TransportRevenueView).all()
    
    #get total sum of value
    total_revenue = db.query(func.sum(models.TransportRevenueView.value)).scalar()
    # Format the total revenue as a currency string
    total_revenue = "${:,.0f}".format(total_revenue)

    if not result:
        raise HTTPException(status_code=404, detail='Can''t get sales data')
    return {
        "records": result,
        "total_revenue": total_revenue
    }