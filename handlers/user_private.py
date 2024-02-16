import emoji

from aiogram import Bot, Dispatcher, F
from aiogram import types, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from getMovies.main_pars import getRandomMovieData


user_private_router = Router()


# Start Command #
@user_private_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Hi, {message.from_user.first_name}! \nI can send you random movie, just enter /movie command"
                         f" for get absolute random movie or choose this command in navbar\n"
                         f"/genre_movie for choose genre and get random movie from this genre")


# Random Movie Command
@user_private_router.message(Command("movie"))
async def get_rnd_movie(message: Message):
    await message.answer(f"Generation Movie {emoji.emojize(':film_projector:')} {emoji.emojize(':clapper_board:')}...")

    movieData = getRandomMovieData()
    movieData.get_full_rnd_movie_data()

    movie_name = movieData.film_name
    movie_genre = movieData.film_genre
    movie_rating = "IBM: " + movieData.film_rating_imb
    movie_desc = movieData.film_desc

    movie_full_desc = f"{movie_name} \n \n{movie_genre} \n \n{movie_rating} \n \n{movie_desc}"
    await message.answer_photo(photo=movieData.poster_img, caption=movie_full_desc)
