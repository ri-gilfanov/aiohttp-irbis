from aiohttp.web import Request
from irbis import Connection

from aiohttp_irbis import IrbisBaseView
from aiohttp_irbis.constants import DEFAULT_KEY


def test_irbis_session(mocked_request: Request, db_session: Connection) -> None:
    mocked_request[DEFAULT_KEY] = db_session
    view = IrbisBaseView(mocked_request)
    assert view.irbis_session() is db_session
