def get_all_genres():

    # genres_en = ['Anime', 'Biography', 'Action movie', 'Western', 'Military', 'Detective', 'Kids', 'Documentary',
    #              'Drama', 'History', 'Comedy', 'Short film', 'Crime', 'Melodrama', 'Music', 'Cartoon', 'Musical',
    #              'Adventure', 'Family', 'Sport', 'Thriller', 'Horror', 'Fantastic', 'Film-Noir', 'Fantasy']

    genres_ru = ['Аниме', 'Биография', 'Боевик', 'Вестерн', 'Военный', 'Детектив', 'Детский', 'Документальный',
                 'Драма', 'История', 'Комедия', 'Короткометражка', 'Криминал', 'Мелодрама', 'Музыка',
                 'Мультфильм', 'Мьюзикл', 'Приключения', 'Семейный', 'Спорт', 'Триллер', 'Ужасы', 'Фантастика',
                 'Фильм-Нуар', 'Фэнтези']

    genres_ru_str = "\n".join(genres_ru)
    # genres_en_str = "\n".join(genres_en)

    return genres_ru_str
