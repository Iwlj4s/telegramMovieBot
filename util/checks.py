def check_genre(user_input_genre, genres):
    user_genres = user_input_genre.split(", ")

    for genre in user_genres:
        if genre in genres:
            return True
    return False


def check_country(user_input_country, countries):
    user_countries = user_input_country.split(", ")

    for country in user_countries:
        if country in countries:
            return True

    return False
