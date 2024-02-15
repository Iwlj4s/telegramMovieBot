import asyncio

import aiogram

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()


# Start Command #
@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Hi!')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
