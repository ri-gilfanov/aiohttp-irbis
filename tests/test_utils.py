from aiohttp.web import Request
from irbis import Connection

from aiohttp_irbis import DEFAULT_KEY, irbis_session


def test_irbis_session(mocked_request: Request, db_session: Connection) -> None:
    mocked_request[DEFAULT_KEY] = db_session
    assert irbis_session(mocked_request) is db_session
