from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Random Movie"),
            KeyboardButton(text="Random Movie By Genre"),
            KeyboardButton(text="Genres")
        ],
    ],
    resize_keyboard=True
)
