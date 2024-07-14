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

countries_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Пропустить поле"),
        ],

        [
            KeyboardButton(text="США"),
            KeyboardButton(text="СССР"),
            KeyboardButton(text="Австралия"),
        ],

        [
            KeyboardButton(text="Бельгия"),
            KeyboardButton(text="Великобритания"),
            KeyboardButton(text="Германия"),
        ],

        [
            KeyboardButton(text="Германия (ФРГ)"),
            KeyboardButton(text="Гонконг"),
            KeyboardButton(text="Индия"),
        ],

        [
            KeyboardButton(text="Испания"),
            KeyboardButton(text="Италия"),
            KeyboardButton(text="Канада"),
        ],

        [
            KeyboardButton(text="Китай"),
            KeyboardButton(text="Корея Южная"),
            KeyboardButton(text="Мексика"),
        ],

        [
            KeyboardButton(text="Франция"),
            KeyboardButton(text="Швеция"),
            KeyboardButton(text="Япония")
        ],

    ]
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

yes_cancel_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Да"),
            KeyboardButton(text="Отмена"),
        ],
    ],
    resize_keyboard=True
)
