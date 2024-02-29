from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Случайный Фильм"),
            KeyboardButton(text="Случайный Фильм По Жанру"),
            KeyboardButton(text="Жанры")
        ],
    ],
    resize_keyboard=True
)
