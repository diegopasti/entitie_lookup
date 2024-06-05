from http import HTTPStatus

from bson.errors import InvalidId

from apps.entities.controllers import PersonController
from apps.entities.schemas import Person

from utils.middlewares import ProcessTimeHeader
from conf.settings import ALLOWED_HOSTS

from fastapi import FastAPI, HTTPException
from fastapi.middleware.trustedhost import TrustedHostMiddleware

app = FastAPI()
app.add_middleware(TrustedHostMiddleware, allowed_hosts=ALLOWED_HOSTS)
app.add_middleware(ProcessTimeHeader)


@app.get("/")
def root():
    return {
        "result": True,
        "message": "Object sucessfully returned",
        "object": {}
    }


@app.get("/person/")
async def filter(query: dict | None = None):

    if query is None:
        query = {}

    try:
        return PersonController().filter(query)

    except InvalidId:
        raise HTTPException(status_code=403, detail="Invalid identifier")


@app.get("/person/{oid}")
async def person(oid):
    try:
        return PersonController().object(oid)

    except InvalidId:
        raise HTTPException(status_code=403, detail="Invalid identifier")


@app.post("/person/", status_code=HTTPStatus.CREATED)
async def insert(data: Person):
    return PersonController().insert(data.dict())


@app.put("/person/{oid}")
async def update(oid: str, data: dict):
    try:
        return PersonController().update(oid, data)

    except InvalidId:
        raise HTTPException(status_code=403, detail="Invalid identifier")


@app.delete("/person/{oid}")
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


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
