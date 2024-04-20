from sqlalchemy import Boolean, MetaData, Column, ForeignKey, Integer, String, Date, DateTime, Float, Enum, UniqueConstraint, \
    Table, DateTime, ARRAY
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship

from database import Base
import datetime


class User(Base):
    __tablename__ = "users"
    username = Column(String(15), primary_key=True, unique=True, nullable=False)
    password = Column(String(), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password



class Fault(Base):
    __tablename__ = "faults"
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    place = Column(String(15), nullable=False)
    room = Column(String(20), nullable=True)
    fault_type = Column(String(20), nullable=False)
    fault_origin = Column(String(20), nullable=False)
    description = Column(String(120), nullable=True)
    priority = Column(Integer, nullable=False)
    fault_date = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, id, place, room, fault_type, fault_origin, description, priority, fault_date):
        self.id = id
        self.place = place
        self.room = room
        self.fault_type = fault_type
        self.fault_origin = fault_origin
        self.description = description
        self.priority = priority
        self.fault_date = fault_date

