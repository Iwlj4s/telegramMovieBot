import asyncio
import logging

import aiogram
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN")

bot = Bot(token=token)
dp = Dispatcher()


# Start Command #
@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Hi, {message.from_user.first_name} !')
    await message.answer_photo(photo='https://image.tmdb.org/t/p/w600_and_h900_bestv2//qYczuua2tgjfxcdtLNDC0n4mOHz.jpg',
                               caption='Poster')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
