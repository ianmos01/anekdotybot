import logging
from aiogram import Bot, Dispatcher, types
from aiogram.client.bot import DefaultBotProperties
from aiogram.filters import CommandStart

from .config import config
from .keyboards import start_keyboard
from .middleware import LoggingMiddleware


async def on_startup(bot: Bot):
    await bot.delete_webhook(drop_pending_updates=True)


async def init() -> None:
    logging.basicConfig(level=logging.INFO)
    bot = Bot(
        token=config.token,
        default=DefaultBotProperties(parse_mode=config.parse_mode),
    )
    dp = Dispatcher()

    dp.message.middleware.register(LoggingMiddleware())

    @dp.message(CommandStart())
    async def cmd_start(message: types.Message) -> None:
        await message.answer("Hello!", reply_markup=start_keyboard())

    await dp.start_polling(bot, on_startup=on_startup)
