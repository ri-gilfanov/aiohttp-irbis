import pytest
from aiohttp import web
from irbis import Connection

import aiohttp_irbis
from aiohttp_irbis import DuplicateAppKeyError, irbis_bind


async def test_duplicate_app_key_error(db_session: Connection) -> None:

    with pytest.raises(DuplicateAppKeyError):
        aiohttp_irbis.setup(web.Application(), [
            irbis_bind(db_session),
            irbis_bind(db_session),
        ])

    with pytest.raises(DuplicateAppKeyError):
        aiohttp_irbis.setup(web.Application(), [
            irbis_bind(db_session, 'irbis_secondary'),
            irbis_bind(db_session, 'irbis_secondary'),
        ])

    aiohttp_irbis.setup(web.Application(), [
        irbis_bind(db_session),
        irbis_bind(db_session, 'irbis_secondary'),
    ])
