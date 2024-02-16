from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Random Movie"),
            KeyboardButton(text="Random Movie By Genre")
        ]
    ]
)