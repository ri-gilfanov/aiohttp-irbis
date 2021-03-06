import toml

from aiohttp_irbis import __version__


def test_version() -> None:
    pyproject = toml.load('./pyproject.toml')
    version = pyproject['tool']['poetry']['version']
    assert __version__ == version
