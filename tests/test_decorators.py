import pytest
from aiohttp.web import Request
from irbis import Connection

from aiohttp_irbis import DuplicateRequestKeyError, irbis_decorator
from aiohttp_irbis.constants import DEFAULT_KEY
from tests.conftest import ClassBasedView, ClassHandler, function_handler


async def test_duplicate_request_key_error(
    mocked_request: Request,
    db_session: Connection,
) -> None:
    assert mocked_request.get(DEFAULT_KEY) is None
    mocked_request[DEFAULT_KEY] = db_session
    assert mocked_request.get(DEFAULT_KEY) is db_session
    with pytest.raises(DuplicateRequestKeyError):
        await irbis_decorator()(function_handler)(mocked_request)


async def test_decorated_class_based_view(mocked_request: Request) -> None:
    assert mocked_request.get(DEFAULT_KEY) is None
    await irbis_decorator()(ClassBasedView.get)(mocked_request)
    assert isinstance(mocked_request.get(DEFAULT_KEY), Connection)


async def test_decorated_class_handler(mocked_request: Request) -> None:
    assert mocked_request.get(DEFAULT_KEY) is None
    await irbis_decorator()(ClassHandler().get)(mocked_request)
    assert isinstance(mocked_request.get(DEFAULT_KEY), Connection)


async def test_decorated_function_handler(mocked_request: Request) -> None:
    assert mocked_request.get(DEFAULT_KEY) is None
    await irbis_decorator()(function_handler)(mocked_request)
    assert isinstance(mocked_request.get(DEFAULT_KEY), Connection)
