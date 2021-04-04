import pytest
from aiohttp.web import Request
from irbis import Connection

from aiohttp_irbis.constants import DEFAULT_KEY
from aiohttp_irbis.exceptions import DuplicateRequestKeyError
from aiohttp_irbis.typedefs import THandler
from tests.conftest import function_handler


async def test_duplicate_request_key_error(
    irbis_main_middleware: THandler,
    mocked_request: Request,
    db_session: Connection,
) -> None:
    assert mocked_request.get(DEFAULT_KEY) is None
    mocked_request[DEFAULT_KEY] = db_session
    assert mocked_request.get(DEFAULT_KEY) is db_session

    with pytest.raises(DuplicateRequestKeyError):
        await irbis_main_middleware(mocked_request, function_handler)


async def test_sa_middleware(
    irbis_main_middleware: THandler,
    mocked_request: Request,
) -> None:
    assert mocked_request.get(DEFAULT_KEY) is None
    await irbis_main_middleware(mocked_request, function_handler)
    assert isinstance(mocked_request.get(DEFAULT_KEY), Connection)
