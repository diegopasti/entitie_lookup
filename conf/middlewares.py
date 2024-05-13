import time
from starlette.middleware.base import BaseHTTPMiddleware


class ProcessTimeHeader(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        """ Return process time in miliseconds (ms) """

        init_time = time.time()
        response = await call_next(request)
        process_time = round((time.time() - init_time)*1000, 2)
        response.headers["X-Process-Time"] = str(process_time)
        return response
