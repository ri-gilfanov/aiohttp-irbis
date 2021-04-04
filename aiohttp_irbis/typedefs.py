from typing import Awaitable, Callable

from aiohttp.web import StreamResponse

THandler = Callable[..., Awaitable[StreamResponse]]
THandlerWrapper = Callable[..., THandler]
