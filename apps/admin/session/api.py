from http import HTTPStatus
from fastapi import APIRouter

from conf.settings import REDIS_URL


router = APIRouter()


@router.get(path="/admin/cache", status_code=HTTPStatus.OK)
async def get_cache_keys():
    """
    Retrieve all keys cached.

    return: List of keys stored in cache
    """

    import redis_cli
    redis_cli.init_from_url(REDIS_URL)
    keys = redis_cli.get_redis().keys()
    return [item.decode('utf-8') for item in keys]


@router.delete(path="/admin/cache", status_code=HTTPStatus.OK)
async def clear_cache():
    """
    Clear data stored in cached.

    return: True or false
    """

    import redis_cli
    redis_cli.init_from_url(REDIS_URL)
    result = redis_cli.get_redis().flushall()
    return result



