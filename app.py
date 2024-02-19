import aiogram
import asyncio

import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.fsm.strategy import FSMStrategy
from dotenv import load_dotenv


from handlers.user_private import user_private_router

load_dotenv()

ALLOWED_UPDATES = ['message', 'edited_message']
token = os.getenv("TOKEN")

bot = Bot(token=token)
dp = Dispatcher()

dp.include_router(user_private_router)


async def main():
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
