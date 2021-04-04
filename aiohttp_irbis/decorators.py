from functools import wraps
from typing import Any

import irbis
from aiohttp.abc import AbstractView
from aiohttp.web import StreamResponse

from aiohttp_irbis.constants import DEFAULT_KEY
from aiohttp_irbis.exceptions import DuplicateRequestKeyError
from aiohttp_irbis.typedefs import THandler, THandlerWrapper


def irbis_decorator(key: str = DEFAULT_KEY) -> THandlerWrapper:
    def wrapper(handler: THandler) -> THandler:
        @wraps(handler)
        async def wrapped(*args: Any, **kwargs: Any) -> StreamResponse:
            request = args[0].request \
                      if isinstance(args[0], AbstractView) \
                      else args[-1]

            irbis.connection.irbis_event_loop = request.app._loop

            if key in request:
                raise DuplicateRequestKeyError(key)

            request[key] = request.config_dict.get(key)
            return await handler(*args, **kwargs)

        return wrapped
    return wrapper
