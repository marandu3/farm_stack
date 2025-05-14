from datetime import date
from pydantic import BaseModel, field_validator
from enum import Enum


class GenreURLChoices(Enum):
    ROCK = 'rock'
    POP = 'pop'
    JAZZ = 'jazz'
    CLASSICAL = 'classical'
    HIP_HOP = 'hip-hop'
    COUNTRY = 'country'


class Album (BaseModel):
    title: str
    release_date: date

class BandBase(BaseModel):
    name:str
    genre:str
    albums: list[Album] = []

class BandCreate(BandBase):
    @field_validator('genre')
    def title_case_genre(cls, value):
        return value.title()

class BandWithID(BandBase):
    id: int
