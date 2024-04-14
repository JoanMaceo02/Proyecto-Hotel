from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

#import models, schemas
#import repository
import os
import sys

#from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

#models.Base.metadata.create_all(bind=engine)  # Creem la base de dades amb els models que hem definit a SQLAlchemy

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
