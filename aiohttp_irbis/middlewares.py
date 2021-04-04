import irbis
from aiohttp.web import Request, StreamResponse, middleware

from aiohttp_irbis.constants import DEFAULT_KEY
from aiohttp_irbis.exceptions import DuplicateRequestKeyError
from aiohttp_irbis.typedefs import THandler


def irbis_middleware(key: str = DEFAULT_KEY) -> THandler:
    """ Irbis asynchronous middleware factory. """
    @middleware
    async def irbis_middleware_(
        request: Request,
        handler: THandler,
    ) -> StreamResponse:
        irbis.connection.irbis_event_loop = request.app._loop

        if key in request:
            raise DuplicateRequestKeyError(key)

        request[key] = request.config_dict.get(key)
        return await handler(request)

    return irbis_middleware_
