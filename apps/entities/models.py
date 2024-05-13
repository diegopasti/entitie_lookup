from pydantic import BaseModel
from typing import Optional


class Entity(BaseModel):

    name: str
    popular_name: str
    nationality: str
    document: str
    birth_foundation: str


class People(Entity):

    profession: Optional[str] = None
    mother_name: Optional[str] = None
    father_name: Optional[str] = None
    children: Optional[int] = 0
