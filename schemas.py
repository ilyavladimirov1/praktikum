from pydantic import BaseModel
from typing import List

class FilmCreate(BaseModel):
    name: str
    year: int
    tags: List[str]
    rating: float

class Film(BaseModel):
    id: int
    name: str
    year: int
    tags: List[str]
    rating: float