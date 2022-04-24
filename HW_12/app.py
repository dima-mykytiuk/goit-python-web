from aiohttp import web
import aiohttp_jinja2
import jinja2
from HW_12.src.routes import setup_routes

app = web.Application()

aiohttp_jinja2.setup(app, loader=jinja2.PackageLoader('src', 'templates'))

setup_routes(app)


if __name__ == "__main__":
    web.run_app(app, host='127.0.0.1', port=8080)
    