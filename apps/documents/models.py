from pydantic import BaseModel
from typing import Optional

from apps.documents.options import DocumentOptions


class Activity(BaseModel):

    code: str
    description: str


class Document(BaseModel):

    type: DocumentOptions
    number: str
    sender: Optional[str]
    expiration_date: Optional[str]
    emission_date: Optional[str]
