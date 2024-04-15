from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


SQLALCHEMY_DATABASE_URL = "sqlite:///./data.db"
#SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Onlypicsdatabase1@db.pnrmoqedbmcpxehltqvy.supabase.co:5432/postgres"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL)
# check_same_thread...is needed only for SQLite. It's not needed for other databases.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()