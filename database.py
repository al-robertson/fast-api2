from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

##DATABASE_URL = 'postgresql://postgres:649809@localhost:5432/dashboard'
DATABASE_URL = 'postgresql://postgres:649809@localhost:5432/DEV_USH?options=-c%20search_path%3Dush_live'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
viewBase = declarative_base()