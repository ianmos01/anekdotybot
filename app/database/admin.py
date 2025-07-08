from aiogram import Bot


async def broadcast(bot: Bot, text: str, user_ids: list[int]):
    for uid in user_ids:
        await bot.send_message(uid, text)
