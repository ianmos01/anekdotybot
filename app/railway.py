import asyncio
import os
from aiohttp import web

from .init import init

async def start_bot():
    # Run bot polling in background
    await init()

async def handle(request: web.Request) -> web.Response:
    return web.Response(text="Bot is running")

async def main() -> None:
    bot_task = asyncio.create_task(start_bot())

    app = web.Application()
    app.add_routes([web.get('/', handle)])

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', int(os.getenv('PORT', 8080)))
    await site.start()

    await bot_task

if __name__ == '__main__':
    asyncio.run(main())
