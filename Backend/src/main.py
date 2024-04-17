from fastapi import Depends, FastAPI, HTTPException, Request
from sqlalchemy.orm import Session

import models, schemas
import repository
import os
import sys

from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

models.Base.metadata.create_all(bind=engine)  # Creem la base de dades amb els models que hem definit a SQLAlchemy

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# Post a new fault
@app.post("/fault", summary="Create new fault", response_model=schemas.FaultBase)
def create_fault(fault: schemas.FaultCreate, db: Session = Depends(get_db)):
    return repository.create_fault(db, fault)


# Get all faults
@app.get("/faults", summary="Get all the faults")
def get_faults(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return repository.get_all_faults(db, skip, limit)


# Get faults of a room
@app.get("/faults/{room}", summary="Get all the faults of a room")
def get_faults_by_room(room: str, db: Session = Depends(get_db)):
    return repository.get_faults_by_room(db, room)
