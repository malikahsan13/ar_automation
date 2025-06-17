from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://user:password@localhost/receivables")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind= engine, autocommit=False, autoflush=False)
Base = declarative_base()