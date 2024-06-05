from http import HTTPStatus

from bson.errors import InvalidId
from fastapi import HTTPException
from fastapi import APIRouter

from apps.entities.controllers import PersonController
from apps.entities.schemas import Person


router = APIRouter()


@router.get(path="/person/", status_code=HTTPStatus.OK)
async def filter(query: dict | None = None):

    if query is None:
        query = {}

    try:
        return PersonController().filter(query)

    except InvalidId:
        raise HTTPException(status_code=403, detail="Invalid identifier")


@router.get("/person/{oid}", status_code=HTTPStatus.OK)
async def person(oid):
    try:
        return PersonController().object(oid)

    except InvalidId:
        raise HTTPException(status_code=403, detail="Invalid identifier")


@router.post("/person/", status_code=HTTPStatus.CREATED)
async def insert(data: Person):
    return PersonController().insert(data.dict())


@router.put("/person/{oid}", status_code=HTTPStatus.CREATED)
async def update(oid: str, data: dict):
    try:
        return PersonController().update(oid, data)

    except InvalidId:
        raise HTTPException(status_code=403, detail="Invalid identifier")


@router.delete("/person/{oid}", status_code=HTTPStatus.NO_CONTENT)
async def delete(oid: str):
    try:
        deleted = PersonController().delete(oid)

        return {
            "result": True,
            "message": "Object deleted successfully",
            "object": deleted
        }

    except InvalidId:
        raise HTTPException(status_code=404, detail="Invalid identifier")