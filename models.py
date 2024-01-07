from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from database import Base
from database import viewBase

class Contacts(Base):
    __tablename__ = 'contacts'

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
    __tablename__ = 'chartdata'

    id = Column(Integer, primary_key=True, index=True)
    classification = Column(String, index=True)
    category = Column(String, index=True)
    value = Column(Integer, index=False)
    attrib1 = Column(String, index=True)
    attrib2 = Column(String, index=True)
    attrib3 = Column(String, index=True)
    recordtimestamp = Column(Date, index=False)
 
class CountrySalesView(viewBase):
    __tablename__ = 'country_sales_view'

    country = Column(String, primary_key=True) 
    category = Column(String, primary_key=True)
    value = Column(Integer)

class TransportRevenueView(viewBase):
    __tablename__ = 'transport_revenue_view'

    country = Column(String, primary_key=True) 
    category = Column(String, primary_key=True)
    value = Column(Integer)
