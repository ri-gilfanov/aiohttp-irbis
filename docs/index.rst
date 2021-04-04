==========================
Документация aiohttp-irbis
==========================
|ReadTheDocs| |PyPI release| |PyPI downloads| |License| |Python versions| |GitHub CI| |Codecov|

.. |ReadTheDocs| image:: https://readthedocs.org/projects/aiohttp-irbis/badge/?version=latest
  :target: https://aiohttp-irbis.readthedocs.io/en/latest/?badge=latest
  :alt: Read The Docs build

.. |PyPI release| image:: https://badge.fury.io/py/aiohttp-irbis.svg
  :target: https://pypi.org/project/aiohttp-irbis/
  :alt: Release

.. |PyPI downloads| image:: https://img.shields.io/pypi/dm/aiohttp-irbis
  :target: https://pypistats.org/packages/aiohttp-irbis
  :alt: PyPI downloads count

.. |License| image:: https://img.shields.io/badge/License-MIT-green
  :target: https://github.com/ri-gilfanov/aiohttp-irbis/blob/master/LICENSE
  :alt: MIT License

.. |Python versions| image:: https://img.shields.io/badge/Python-3.7%20%7C%203.8%20%7C%203.9-blue
  :target: https://pypi.org/project/aiohttp-irbis/
  :alt: Python version support

.. |GitHub CI| image:: https://github.com/ri-gilfanov/aiohttp-irbis/actions/workflows/ci.yml/badge.svg?branch=master
  :target: https://github.com/ri-gilfanov/aiohttp-irbis/actions/workflows/ci.yml
  :alt: GitHub continuous integration

.. |Codecov| image:: https://codecov.io/gh/ri-gilfanov/aiohttp-irbis/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/ri-gilfanov/aiohttp-irbis
  :alt: codecov.io status for master branch

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Обзор
-----
Пакет, связывающий библиотеку PythonIrbis с асинхронным веб-фреймворком aiohttp.

Установка
---------
::

  pip install aiohttp-irbis

Пример
------
.. code-block:: python

  from aiohttp import web
  import aiohttp_irbis
  from aiohttp_irbis import irbis_bind
  from irbis import Connection


  async def main(request):

      async with request['irbis_main'] as conn:
          found = await conn.search_async('"A=Пушкин$"')
          return web.json_response({'result': found})


  app = web.Application()

  connection = Connection()
  connection.parse_connection_string(';'.join([
      f'host={input("Введите адрес сервера: ")}',
      f'port={input("Введите порт сервера: ")}',
      f'username={input("Введите имя пользователя: ")}',
      f'password={input("Введите пароль пользователя: ")}',
      f'db={input("Введите название базы данных: ")}',
  ]))

  aiohttp_irbis.setup(app, [irbis_bind(connection)])

  app.add_routes([web.get('/', main)])
  web.run_app(app)


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
