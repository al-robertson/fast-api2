from pydantic import BaseModel
from typing import Optional

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

class APIRouteBase(BaseModel):
    method: str
    path: str
    description: Optional[str] = None

class APIRouteCreate(APIRouteBase):
    auth_info: Optional[str] = None
    parameters: Optional[dict] = None

class APIRoute(APIRouteBase):
    id: int
    auth_info: Optional[str] = None
    parameters: Optional[dict] = None

    class Config:
        orm_mode = True