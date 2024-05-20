from typing import List

from sqlalchemy.orm import Session
from models import Film, Tag
from schemas import FilmCreate


def get_film(db: Session, film_id: int):
    return db.query(Film).filter(Film.id == film_id).first()


def get_films(db: Session, year: int = None, tags: List[str] = []):
    query = db.query(Film)
    if year:
        query = query.filter(Film.year == year)
    if tags:
        query = query.join(Film.tags).filter(Tag.name.in_(tags))
    return query.all()


def create_film(db: Session, film: FilmCreate):
    tags = [Tag(name=tag_name) for tag_name in film.tags]
    new_film = Film(title=film.name, year=film.year, rating=film.rating, tags=tags)
    db.add(new_film)
    db.commit()
    db.refresh(new_film)
    return new_film


def update_film(db: Session, film_id: int, film: FilmCreate):
    db_film = get_film(db, film_id)
    db_film.title = film.name
    db_film.year = film.year
    db_film.rating = film.rating
    db.commit()
    db.refresh(db_film)
    return db_film


def delete_film(db: Session, film_id: int):
    db_film = get_film(db, film_id)
    db.delete(db_film)
    db.commit()
    return db_film
