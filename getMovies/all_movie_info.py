from getMovies.main_pars import GetRandomMovieData


def movie_info(genre_name: str, genre: bool):
    movieData = GetRandomMovieData()
    movieData.get_movie_data(genre_name, genre)

    movie_poster = movieData.poster_img
    movie_name = movieData.film_name
    movie_genre = movieData.film_genre
    movie_rating = "IBM: " + movieData.film_rating_imb
    movie_desc = movieData.film_desc

    movie_full_desc = f"{movie_name} \n \n{movie_genre} \n \n{movie_rating} \n \n{movie_desc}"

    return movie_poster, movie_full_desc
