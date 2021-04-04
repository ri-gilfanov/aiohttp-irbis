from abc import ABCMeta

from aiohttp.abc import AbstractView
from aiohttp.web import View
from irbis import Connection

from aiohttp_irbis.constants import DEFAULT_KEY


class IrbisAbstractView(AbstractView, metaclass=ABCMeta):
    """
    Simple SQLAlchemy view based on aiohttp.abc.AbstractView.

    The `__await__` method must be implemented in child classes.

    Suitable for a specific usage with multiple models.
    """
    def irbis_session(self, key: str = DEFAULT_KEY) -> Connection:
        return self.request[key]


class IrbisBaseView(View, IrbisAbstractView):
    """
    Simple SQLAlchemy view based on aiohttp.web.View.

    Recomended for a specific usage with multiple models.
    """
