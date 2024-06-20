import json

from http import HTTPStatus
from typing import List

from bson.errors import InvalidId
from fastapi import HTTPException, APIRouter, Request
from fastapi_cache import FastAPICache
from starlette.responses import JSONResponse

from apps.entities.controllers import PersonController
from utils.caches import custom_key_builder

router = APIRouter()


@router.get(path="/person", status_code=HTTPStatus.OK)
async def filter(query: dict | None = None,  request: Request = None):
    """
    Returns records of people that meet the specified parameters or all records if no query is provided.

    :param query: Optional dictionary containing the fields and values that will be used in the query

    :param request: Request properties

    return: List of records that have the searched parameters, or empty list if there are no records that match
    """

    redis = FastAPICache.get_backend()
    key = custom_key_builder(filter, request=request, namespace="entities", kwargs=query)
    cache_control = request.headers.get("Cache-Control")
    headers = {"Cache-Control": "max-age=3600"}

    if cache_control != "no-cache":
        cached = await redis.get(key)

        if cached:
            return JSONResponse(content=json.loads(cached), headers=headers)

    if query is None:
        query = {}

    try:
        response = PersonController().filter(query, format=False)
        data = json.dumps(response, default=str)

        if cache_control != "no-cache":
            one_hour = 60 * 60
            await redis.set(key, data, expire=one_hour)

        return JSONResponse(content=json.loads(data), headers=headers)

    except InvalidId:
        raise HTTPException(status_code=403, detail="Invalid identifier")


@router.get("/person/{oid}", status_code=HTTPStatus.OK)
async def object(oid: str):
    """
    Returns a dictionary containing the data of the searched record or empty if
    there are no records with the given identifier.

    :param oid: ObjectID of the record that will be searched

    return: Dictionary with record data or empty
    """

    try:
        return PersonController().object(oid)

    except InvalidId:
        raise HTTPException(status_code=403, detail="Invalid identifier")


@router.post("/person/", status_code=HTTPStatus.CREATED)
async def insert(data: List[dict]):
    """
    Return a dictionary list containing the inserted records.

    :param data: ObjectID of the record that will be searched

    return: Dictionary with record data or empty
    """
    response = PersonController().insert(data)
    return response


@router.put("/person/", status_code=HTTPStatus.CREATED)
async def update(query: dict, data: dict):
    try:
        return PersonController().update(query, data)

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


@router.get(path="/generate/", status_code=HTTPStatus.OK)
async def generate(quant: int = 1):
    """
    Create one or more new random entity(s).

    :param quant: Quantity of new objects, default is 1.

    return: List of created objects
    """

    return PersonController().generate(quant)

