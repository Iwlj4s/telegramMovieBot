import emoji

# Aiogram Imports #
from aiogram import F, Router

from aiogram.filters import CommandStart, Command, StateFilter, or_f

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from aiogram.types import Message

# My Imports #
from getMovies.all_movie_info import movie_info
from genres.checks import check_genre
from genres.genres import get_all_genres

from keyboards.reply import main_keyboard, genres_keyboard, yes_no_cancel_keyboard

user_private_router = Router()

genres_ru_str = get_all_genres()


# FSM
class GetUserGenre(StatesGroup):
    user_genres = []

    user_genre = State()
    user_genre_confirm = State()


# Start Command #
@user_private_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}! \n"
        f"\nЧтобы посмотреть жанры выберите в кнопочном меню 'Жанры \n"
        f"\nЧтобы получить случайный фильм или выберите в кнопочном меню 'Случайный Фильм'\n"
        f"\nЧтобы получить случайный фильм по выбранному жанру выберите в кнопочном меню 'Случайный Фильм По Жанру'\n",
        reply_markup=main_keyboard
    )


# Cancel #
@user_private_router.message(StateFilter("*"), F.text.lower() == "отмена")
async def cancel_handler(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.clear()
    await message.answer("Все действия отменены",
                         reply_markup=main_keyboard)


# Genres Info #
@user_private_router.message(or_f(Command("genres"), (F.text.lower() == "жанры")))
async def get_genres(message: Message):
    await message.answer(f"Жанры:\n{genres_ru_str}")


# Random Movie Command
@user_private_router.message(or_f(Command("movie"), (F.text.lower() == "случайный фильм")))
async def get_rnd_movie(message: Message):
    await message.answer(f"Генерация фильма {emoji.emojize(':film_projector:')} {emoji.emojize(':clapper_board:')}...")

    poster, movie_full_info = movie_info(genre_name="", genre=False)

    await message.answer_photo(photo=poster, caption=movie_full_info,
                               reply_markup=main_keyboard)


# Random Movie by Selected Genre #
@user_private_router.message(F.text.lower() == "случайный фильм по жанру")
@user_private_router.message(StateFilter(None), Command("genre_movie"))
async def get_genre_rnd_movie(message: Message, state: FSMContext):
    await message.answer("Введите Жанр: ",
                         reply_markup=genres_keyboard)
    await state.set_state(GetUserGenre.user_genre)


@user_private_router.message(GetUserGenre.user_genre)
async def user_send_genre(message: Message, state: FSMContext):
    data = await state.get_data()
    user_genres = data.get("user_genres", [])
    user_genres.append(message.text.lower())
    await state.update_data(user_genres=user_genres)

    await message.answer("Вы хотите добавить еще жанр?",
                         reply_markup=yes_no_cancel_keyboard)
    await state.set_state(GetUserGenre.user_genre_confirm)


@user_private_router.message(GetUserGenre.user_genre_confirm, F.text.lower() == "да")
async def user_genre_more(message: Message, state: FSMContext):
    await message.answer("Введите Жанр: ",
                         reply_markup=genres_keyboard)
    await state.set_state(GetUserGenre.user_genre)


@user_private_router.message(GetUserGenre.user_genre_confirm, F.text.lower() == "нет")
async def user_genre_done(message: Message, state: FSMContext):
    data = await state.get_data()
    user_genres = data.get("user_genres", [])

    print(f"User input genres: {user_genres}")
    print(f"Available genres: {genres_ru_str.lower()}")

    valid_genres = [genre for genre in user_genres if check_genre(user_input_genre=genre, genres=genres_ru_str.lower())]

    print(f"Valid genres: {valid_genres}")

    if valid_genres:
        await message.answer(f"Выбранные Жанры: {','.join(valid_genres)}")
        await message.answer(
            f"Генерация фильма {emoji.emojize(':clapper_board:')} ...")

        poster, movie_full_info = movie_info(genre_name=','.join(valid_genres), genre=True)

        await message.answer_photo(photo=poster, caption=movie_full_info,
                                   reply_markup=main_keyboard)
    else:
        await message.answer(
            f"{message.from_user.first_name}, введите корректные жанры\n/genres чтобы посмотреть жанры")

    await state.clear()
