from aiohttp.web import Request
from irbis import Connection

from aiohttp_irbis.constants import DEFAULT_KEY


def irbis_session(request: Request, key: str = DEFAULT_KEY) -> Connection:
    return request[key]
