import aiohttp
from aiohttp import web
import sqlite3

async def auth_middleware(app, handler):
    async def middleware(request):
        # Perform authentication here, e.g., checking for an API key in the request headers
        api_key = request.headers.get('API-Key')
        if not api_key or api_key != 'your_api_key':
            return web.Response(text="Unauthorized", status=401)
        
        # Continue to the main handler if authentication passes
        return await handler(request)
    return middleware

async def handle(request):
    return web.Response(text="Hello, this is an aiohttp server!")

async def get_data(request):
    conn = request.app['db_connection']
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM your_table")
    data = cursor.fetchall()
    return web.json_response({'data': data})

app = web.Application(middlewares=[auth_middleware])

app.router.add_get('/', handle)
app.router.add_get('/get_data', get_data)

async def on_startup(app):
    app['db_connection'] = sqlite3.connect('your_database.db')

async def on_cleanup(app):
    app['db_connection'].close()

app.on_startup.append(on_startup)
app.on_cleanup.append(on_cleanup)

web.run_app(app, host="0.0.0.0", port=8080)
