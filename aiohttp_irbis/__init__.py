from typing import Iterable, Tuple

from aiohttp.web import Application
from irbis import Connection

from aiohttp_irbis.constants import DEFAULT_KEY
from aiohttp_irbis.decorators import irbis_decorator
from aiohttp_irbis.exceptions import (
    DuplicateAppKeyError,
    DuplicateRequestKeyError,
)
from aiohttp_irbis.middlewares import irbis_middleware
from aiohttp_irbis.utils import irbis_session
from aiohttp_irbis.views import IrbisAbstractView, IrbisBaseView

TIrbisBinding = Tuple[Connection, str, bool]


__version__ = '0.1dev0'

__all__ = ['DEFAULT_KEY', 'DuplicateAppKeyError', 'DuplicateRequestKeyError',
           'IrbisAbstractView', 'IrbisBaseView', 'irbis_bind',
           'irbis_decorator', 'irbis_middleware', 'irbis_session', 'setup']


def irbis_bind(connection: Connection, key: str = DEFAULT_KEY, *,
               middleware: bool = True) -> TIrbisBinding:
    return connection, key, middleware


def setup(app: Application, bindings: Iterable[TIrbisBinding]) -> None:
    for connection, key, middleware in bindings:
        if key in app:
            raise DuplicateAppKeyError(key)
        app[key] = connection

        if middleware:
            app.middlewares.append(irbis_middleware(key))
