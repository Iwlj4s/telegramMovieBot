from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Случайный Фильм"),
            KeyboardButton(text="Случайный Фильм По Жанру"),
            KeyboardButton(text="Случайный Фильм По Жанру с доп.опциями"),
            KeyboardButton(text="Жанры")
        ],
    ],
    resize_keyboard=True
)


genres_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Аниме"),
            KeyboardButton(text="Биография"),
            KeyboardButton(text="Боевик"),
            KeyboardButton(text="Вестерн"),
        ],

        [
            KeyboardButton(text="Военный"),
            KeyboardButton(text="Детектив"),
            KeyboardButton(text="Детский"),
            KeyboardButton(text="Документальный"),
        ],

        [
            KeyboardButton(text="Драма"),
            KeyboardButton(text="Мультфильм"),
            KeyboardButton(text="Мюзикл"),
            KeyboardButton(text="Приключения"),
        ],

        [
            KeyboardButton(text="Семья"),
            KeyboardButton(text="Спорт"),
            KeyboardButton(text="Триллер"),
            KeyboardButton(text="Ужасы"),
        ],

        [
            KeyboardButton(text="Фантастика"),
            KeyboardButton(text="Фэнтези"),
        ]
    ],
    resize_keyboard=True
)

yes_no_cancel_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Да"),
            KeyboardButton(text="Нет"),
            KeyboardButton(text="Отмена"),
        ],
    ],
    resize_keyboard=True
)

