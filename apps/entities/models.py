from pydantic import BaseModel
from typing import Optional

from apps.documents.models import Activity, Document


class Entity(BaseModel):

    name: str
    popular_name: str
    nationality: str
    documents: str
    birth_foundation: str
    documents: Optional[Document] = []


class People(Entity):

    profession: Optional[str] = None
    mother_name: Optional[str] = None
    father_name: Optional[str] = None
    children: Optional[int] = 0


class Company(Entity):

    activities: Optional[Activity] = None

