from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from typing import Callable, Awaitable, Any


class LoggingMiddleware(BaseMiddleware):
    async def __call__(self, handler: Callable[[TelegramObject], Awaitable[Any]], event: TelegramObject) -> Any:
        print(f"Handling event: {event}")
        return await handler(event)
