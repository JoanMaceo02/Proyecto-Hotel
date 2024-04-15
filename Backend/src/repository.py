from sqlalchemy.orm import Session
import models, schemas
from datetime import datetime



# Create new fault

def create_fault(db: Session, fault: schemas.FaultCreate):
    db_fault = models.Fault(id=fault.id, place=fault.place, room=fault.room, fault_type=fault.fault_type, fault_origin= fault.fault_origin,
                            description=fault.description, priority=fault.priority, fault_date=fault.fault_date)

    try:
        db.add(db_fault)
        db.commit()
        db.refresh(db_fault)
        return db_fault
    except:
        db.rollback()
        return {"message": "An error occurred inserting the fault into the database."}, 500