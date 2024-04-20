from sqlalchemy.orm import Session
import models, schemas
from datetime import datetime



# Create new user
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username, password=user.password)

    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except:
        db.rollback()
        return {"message": "An error occurred inserting the user into the database."}, 500

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


# Get all faults
def get_all_faults(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Fault).offset(skip).limit(limit).all()


# Get fault by id
def get_fault(db: Session, fault_id: int):
    return db.query(models.Fault).filter(models.Fault.id == fault_id).first()


# Get all the faults of a room
def get_faults_by_room(db: Session, room: str):
    return db.query(models.Fault).filter(models.Fault.room == room)