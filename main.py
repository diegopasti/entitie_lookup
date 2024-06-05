from fastapi import FastAPI
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from apps.entities.api import router as entities_router
from utils.middlewares import ProcessTimeHeader
from conf.settings import ALLOWED_HOSTS

app = FastAPI()
app.add_middleware(TrustedHostMiddleware, allowed_hosts=ALLOWED_HOSTS)
app.add_middleware(ProcessTimeHeader)
app.include_router(entities_router)


@app.get("/")
def root():
    return {
        "result": True,
        "message": "Object sucessfully returned",
        "object": {}
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
