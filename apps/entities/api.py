from http import HTTPStatus
from typing import List

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
async def insert(data: List[Person]):
    print("VAMOS INSERIR MULTIPLAS PESSOAS:", data)
    response = PersonController().insert(data)
    print("VEJA A RESPOSTA", response)
    return response


@router.put("/person/", status_code=HTTPStatus.CREATED)
async def update(query: dict, data: dict):
    try:
        updated = PersonController().update(query, data)
        print("VEJA O QUE TEM UPDATED:", updated)
        return updated

    except InvalidId:
        raise HTTPException(status_code=403, detail="Invalid identifier")


@router.delete("/person/", status_code=HTTPStatus.NO_CONTENT)
async def delete(query: dict):
    try:
        deleted = PersonController().delete(query)

        return {
            "result": True,
            "message": "Object deleted successfully",
            "object": deleted
        }

    except InvalidId:
        raise HTTPException(status_code=404, detail="Invalid identifier")
