from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import JSON  # This is specifically for PostgreSQL

from database import Base
from database import viewBase

class Contacts(Base):
    __tablename__ = 'tmp_contacts'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    age = Column(Integer, index=True)
    phone = Column(String, index=True)
    address = Column(String, index=True)
    city = Column(String, index=True)
    zipCode = Column(String, index=True)
    registrarId = Column(Integer, index=True)

class ChartData(Base):
    __tablename__ = 'tmp_chartdata'

    id = Column(Integer, primary_key=True, index=True)
    classification = Column(String, index=True)
    category = Column(String, index=True)
    value = Column(Integer, index=False)
    attrib1 = Column(String, index=True)
    attrib2 = Column(String, index=True)
    attrib3 = Column(String, index=True)
    recordtimestamp = Column(Date, index=False)
 
class CountrySalesView(viewBase):
    __tablename__ = 'tmp_country_sales_view'

    country = Column(String, primary_key=True) 
    category = Column(String, primary_key=True)
    value = Column(Integer)

class TransportRevenueView(viewBase):
    __tablename__ = 'tmp_transport_revenue_view'

    country = Column(String, primary_key=True) 
    category = Column(String, primary_key=True)
    value = Column(Integer)

class APIRoute(Base):
    __tablename__ = "api_routes"

    id = Column(Integer, primary_key=True, index=True)
    method = Column(String, nullable=False)
    path = Column(String, nullable=False)
    auth_info = Column(String)  # Adjust based on encryption approach
    description = Column(String)
    parameters = Column(JSON)