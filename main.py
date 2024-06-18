from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis

from apps.entities.api_restfull import router as entities_router
from apps.admin.session.api import router as admin_router
from utils.middlewares import ProcessTimeHeader
from conf.settings import ALLOWED_HOSTS, REDIS_URL


@asynccontextmanager
async def startup(app: FastAPI):
    redis = aioredis.from_url(REDIS_URL, encoding="utf8", decode_responses=False)
    FastAPICache.init(RedisBackend(redis), prefix="entity_lookup")
    yield


app = FastAPI(
    title="Entity Lookup",
    description="Webservice to consult data from people registered on the platform",
    summary="",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Diego Pasti",
        "url": "https://github.com/diegopasti",
        "email": "diegopasti@gmail.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://github.com/diegopasti/entities_lookup/blob/main/LICENSE",
    },
    lifespan=startup
)

app.add_middleware(TrustedHostMiddleware, allowed_hosts=ALLOWED_HOSTS)
app.add_middleware(ProcessTimeHeader)
app.include_router(admin_router, tags=["admin"])
app.include_router(entities_router, tags=["person"])


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
