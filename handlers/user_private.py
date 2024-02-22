import emoji

# Aiogram Imports #
from aiogram import F, Router

from aiogram.filters import CommandStart, Command, StateFilter, or_f

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from aiogram.types import Message

# My Imports #
from getMovies.all_movie_info import movie_info
from common.genres.checks import check_genre
from common.genres.genres import get_all_genres

from keyboards.reply import main_keyboard

user_private_router = Router()

genres_str = get_all_genres()


# FSM
class get_user_genre(StatesGroup):
    user_genre = State()


# Start Command #
@user_private_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Hi, {message.from_user.first_name}! \n/genres for check genres "
                         f"or choose it in on buttons\n \n"
                         f"/movie for get absolute random movie or choose it on buttons\n \n"
                         f"/genre_movie for choose genre and get random movie from this genre or choose it on buttons",
                         reply_markup=main_keyboard)


# Genres Info #
@user_private_router.message(or_f(Command("genres"), (F.text.lower() == "genres")))
async def get_genres(message: Message):
    await message.answer(f"Genres:\n{genres_str}")


# Random Movie Command
@user_private_router.message(or_f(Command("movie"), (F.text.lower() == "random movie")))
async def get_rnd_movie(message: Message):
    await message.answer(f"Generation Movie {emoji.emojize(':film_projector:')} {emoji.emojize(':clapper_board:')}...")

    poster, movie_full_info = movie_info(genre_name="", genre=False)

    await message.answer_photo(photo=poster, caption=movie_full_info)


# Random Movie by Selected Genre #
@user_private_router.message(F.text.lower() == "random movie by genre")
@user_private_router.message(StateFilter(None), Command("genre_movie"))
async def get_genre_rnd_movie(message: Message, state: FSMContext):
    await message.answer("Write movie genre: ")

    await state.set_state(get_user_genre.user_genre)


# Get user genre #
@user_private_router.message(get_user_genre.user_genre)
async def user_send_genre(message: Message, state: FSMContext):
    await state.update_data(user_selected_genre=message.text.lower())

    data = await state.get_data()
    user_selected_genre = data.get("user_selected_genre")

    # User input in genres?
    if check_genre(user_input_genre=user_selected_genre.lower(), genres=genres_str.lower()):

        await message.answer(f"Selected Genre: {user_selected_genre}")
        await message.answer(f"Generation Movie {emoji.emojize(':film_projector:')}"
                             f"{emoji.emojize(':clapper_board:')}...")

        poster, movie_full_info = movie_info(genre_name=str(user_selected_genre), genre=True)

        await message.answer_photo(photo=poster, caption=movie_full_info)

        await state.clear()

    else:
        await state.clear()
        await message.answer("Please enter correct genre\n/genres for check genres ")

