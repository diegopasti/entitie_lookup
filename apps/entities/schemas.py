from pydantic import BaseModel
from typing import Optional, List

from apps.documents.models import Activity, Document


class Entity(BaseModel):
    identifier: str
    name: str
    popular_name: Optional[str] = None
    nationality: Optional[str] = None
    birth_foundation: Optional[str] = None
    documents: Optional[List[Document]] = None
    address: Optional[List[dict]]


class Person(Entity):

    profession: Optional[str] = None
    mother_name: Optional[str] = None
    father_name: Optional[str] = None
    children: Optional[int] = 0


class Company(Entity):

    activities: Optional[Activity] = None

