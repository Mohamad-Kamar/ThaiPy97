from aiohttp import web

async def handle(request):
    return web.Response(text="Hello, this is an aiohttp server!")

app = web.Application()
app.router.add_get('/', handle)

web.run_app(app)
