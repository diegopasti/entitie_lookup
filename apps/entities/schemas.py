from pydantic import BaseModel
from typing import Optional

from apps.documents.models import Activity, Document


class Entity(BaseModel):

    name: str
    popular_name: Optional[str] = None
    nationality: Optional[str] = None
    birth_foundation: Optional[str] = None
    documents: Optional[Document] = None


class Person(Entity):

    profession: Optional[str] = None
    mother_name: Optional[str] = None
    father_name: Optional[str] = None
    children: Optional[int] = 0


class Company(Entity):

    activities: Optional[Activity] = None

