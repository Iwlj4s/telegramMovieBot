def check_genre(user_input_genre, genres):
    user_genres = user_input_genre.split(", ")

    for genre in user_genres:
        if genre in genres:
            return True
    return False

