from pydantic import BaseModel

class ContactResponse(BaseModel):
    id: int
    name: str
    email: str
    age: int
    phone: str
    address: str
    city: str
    zipCode: str
    registrarId: int 

class ContactCreate(BaseModel):
    name: str
    email: str
    age: int
    phone: str
    address: str
    city: str
    zipCode: str
    registrarId: int