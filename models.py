from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base


DB_URL = "sqlite:///movies_info.db"
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Film(Base):
    __tablename__ = "films"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    tags = relationship('Tag', secondary='film_tags', back_populates='films')


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    films = relationship('Film', secondary='film_tags', back_populates='tags')


class FilmTag(Base):
    __tablename__ = "film_tags"

    film_id = Column(Integer, ForeignKey('films.id'), primary_key=True)
    tag_id = Column(Integer, ForeignKey('tags.id'), primary_key=True)
