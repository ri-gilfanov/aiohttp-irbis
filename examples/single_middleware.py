from aiohttp import web
from irbis import Connection

import aiohttp_irbis
from aiohttp_irbis import irbis_bind


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
