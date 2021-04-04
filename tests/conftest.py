import pytest
from aiohttp.hdrs import METH_GET
from aiohttp.test_utils import make_mocked_request
from aiohttp.web import Application, Request, Response, View, json_response
from irbis import Connection

import aiohttp_irbis
from aiohttp_irbis import irbis_bind, irbis_middleware
from aiohttp_irbis.typedefs import THandler

pytest_plugins = 'aiohttp.pytest_plugin'


@pytest.fixture
def db_session() -> Connection:
    return Connection()


@pytest.fixture
def irbis_main_middleware() -> THandler:
    return irbis_middleware('irbis_main')


@pytest.fixture
def middlewared_app(db_session: Connection) -> Application:
    app = Application()
    aiohttp_irbis.setup(app, [irbis_bind(db_session)])
    return app


@pytest.fixture
def mocked_request(middlewared_app: Application) -> Request:
    return make_mocked_request(METH_GET, '/', app=middlewared_app)


async def function_handler(request: Request) -> Response:
    return json_response({})


class ClassHandler:
    async def get(self, request: Request) -> Response:
        return json_response({})


class ClassBasedView(View):
    async def get(self) -> Response:
        return json_response({})
