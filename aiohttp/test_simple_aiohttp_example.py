import pytest
from aiohttp import web
from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop

class MyAioHTTPTest(AioHTTPTestCase):

    async def get_application(self):
        app = web.Application()
        app.router.add_get('/', self.handle)
        return app

    @unittest_run_loop
    async def test_handle(self):
        request = await self.client.get('/')
        assert request.status == 200
        text = await request.text()
        assert 'Hello, this is an aiohttp server!' in text

    async def handle(self, request):
        return web.Response(text="Hello, this is an aiohttp server!")

if __name__ == '__main__':
    pytest.main()
