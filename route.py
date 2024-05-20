from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import SessionLocal
import crud
import schemas

router = APIRouter()


@router.get("/film", response_model=List[schemas.Film])
def get_films(year: int = None, tags: List[str] = []):
    db: Session = Depends(SessionLocal)
    return crud.get_films(db, year, tags)


@router.get("/film/{film_id}", response_model=schemas.Film)
def get_film(film_id: int):
    db: Session = Depends(SessionLocal)
    return crud.get_film(db, film_id)


@router.post("/film/", response_model=schemas.Film)
def create_film(film: schemas.FilmCreate):
    db: Session = Depends(SessionLocal)
    return crud.create_film(db, film)


@router.put("/film/{film_id}", response_model=schemas.Film)
def update_film(film_id: int, film: schemas.FilmCreate):
    db: Session = Depends(SessionLocal)
    return crud.update_film(db, film_id, film)


@router.delete("/film/{film_id}", response_model=schemas.Film)
def delete_film(film_id: int):
    db: Session = Depends(SessionLocal)
    return crud.delete_film(db, film_id)
