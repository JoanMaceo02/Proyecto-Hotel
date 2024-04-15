import enum
from pydantic import BaseModel, Field, validator
import re
from typing import Optional, List
from datetime import datetime

class FaultBase(BaseModel):
    id: int
    place: str
    room: str
    fault_type: str
    fault_origin: str
    description: str
    priority: int
    fault_date : datetime

    class Config:
        from_attributes = True

class FaultCreate(FaultBase):
    pass