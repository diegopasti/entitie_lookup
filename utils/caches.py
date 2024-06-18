import hashlib
from typing import Callable, Optional

from starlette.requests import Request
from starlette.responses import Response


def custom_key_builder(
        func: Callable, user: Optional[str] = "", namespace: Optional[str] = "", request: Optional[Request] = None,
        response: Optional[Response] = None, args: Optional[tuple] = None, kwargs: Optional[dict] = None,
        ) -> str:

    """
    Custom generation key for store values in cache

    :param func:
    :param user:
    :param namespace:
    :param request:
    :param response:
    :param args:
    :param kwargs:
    :return:
    """

    from fastapi_cache import FastAPICache

    prefix = ""
    if user:
        prefix += f"{user}>"

    prefix += f"{FastAPICache.get_prefix()}:{namespace}:{func.__name__}:"
    return (
        prefix
        + hashlib.md5(
            f"{request.url}:{args}:{kwargs}".encode()
        ).hexdigest()
    )
