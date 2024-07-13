import requests
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


class ParsSettings:
    def __init__(self):
        self.url = "https://www.kinopoisk.ru/chance/"
        self.url_for_img = "https://www.kinopoisk.ru/"

        self.response = requests.get(self.url)
        self.driver = webdriver.Chrome()

        self.user_genre_key = []

        # self.genres_en = {
        #     '1750': 'anime', '22': 'biography',
        #     '3': 'action movie', '13': 'western',
        #     '19': 'military', '17': 'detective',
        #     '456': 'kids', '12': 'documentary',
        #     '8': 'drama', '23': 'history',
        #     '6': 'comedy', '15': 'short film',
        #     '16': 'crime', '7': 'melodrama',
        #     '21': 'music', '14': 'cartoon',
        #     '9 ': 'musical', '10': 'adventure',
        #     '11': 'family', '24': 'sport',
        #     '4': 'thriller', '1': 'horror',
        #     '2': 'fantastic', '18': 'film-noir',
        #     '5': 'fantasy'
        # }

        self.genres_ru = {
            '1750': 'аниме', '22': 'биография',
            '3': 'боевик', '13': 'вестерн',
            '19': 'военный', '17': 'детектив',
            '456': 'детский', '12': 'документальный',
            '8': 'драма', '23': 'история',
            '6': 'комедия', '15': 'короткометражка',
            '16': 'криминал', '7': 'мелодрама',
            '21': 'музыка', '14': 'мультфильм',
            '9 ': 'мьюзикл', '10': 'приключения',
            '11': 'семейный', '24': 'спорт',
            '4': 'триллер', '1': 'ужасы',
            '2': 'фантастика', '18': 'фильм-нуар',
            '5': 'фэнтези'
        }


class Driver(ParsSettings):
    def __init__(self):
        super().__init__()
        self.driver.get(self.url)

        self.genre_list = self.driver.find_element(By.ID, "genreListTitle")
        self.country_list = self.driver.find_element(By.ID, "countryListTitle")
        self.button = self.driver.find_element(By.CLASS_NAME, "button")

        self.new_html = None
        self.soup = None

    def find_user_gener(self, genres):
        """

        :param genres: dict genre, keys == value in HTML || values == genres
        :return: genre key by user input genre, like: Anime: 1750
        """
        print("User input: ", genres)
        for genre in genres:
            genre = genre.strip()
            for key in self.genres_ru:
                if self.genres_ru[key] == genre:
                    self.user_genre_key.append(key)
        print("Genre Keys: ", self.user_genre_key)
        return self.user_genre_key

    def get_rnd_movie(self):
        """
        click on "get movie" button
        :return new HTML page with movie
        """
        self.button.click()
        self.new_html = self.driver.page_source
        self.soup = BeautifulSoup(self.new_html, "lxml")
        self.driver.quit()
        return self.soup

    def get_rnd_gener_movie(self, u_genres):
        """
        u_gener => find_user_gener(gener)
        :return new HTML page with movie
        """
        self.find_user_gener(u_genres)
        self.genre_list.click()

        time.sleep(3)
        print(self.user_genre_key)
        for key in self.user_genre_key:
            self.driver.find_element(By.XPATH, f"//input[@value='{key}']").click()
            time.sleep(5)
        time.sleep(5)

        self.button.click()

        self.new_html = self.driver.page_source
        self.soup = BeautifulSoup(self.new_html, "lxml")

        self.driver.quit()
        return self.soup


class GetRandomMovieData(Driver, ParsSettings):
    def __init__(self):
        super().__init__()
        self.poster_div = None
        self.poster_img_href = None
        self.poster_img = None

        self.film_name_div = None
        self.film_name = None

        self.film_genre_div = None
        self.film_genre = None

        self.film_rating_div = None
        self.film_rating_imb = None

        self.film_desc_div = None
        self.film_desc = None

    def get_movie_data(self, user_gener, genre=False):
        """
        :param user_gener:  => get_rnd_gener_movie(u_gener)
        :param genre: If false: get random movie with random genre Else: get random movie with selected genre
        """
        self.soup = None

        if not genre:
            self.soup = self.get_rnd_movie()
        elif genre:
            self.soup = self.get_rnd_gener_movie(user_gener)

        self.poster_div = self.soup.find("div", class_="poster")
        self.poster_img_href = self.poster_div.find("img")["src"]
        self.poster_img = self.url_for_img + self.poster_img_href

        self.film_name_div = self.soup.find("div", class_="filmName")
        self.film_name = self.film_name_div.find("a").text

        self.film_genre_div = self.soup.find("div", class_="gray")
        self.film_genre = self.film_genre_div.text.strip()

        self.film_rating_div = self.soup.find("div", class_="rating")
        self.film_rating_imb = self.film_rating_div.text.strip()

        self.film_desc_div = self.soup.find("div", class_="syn")
        self.film_desc = self.film_desc_div.text.strip()


# movie_data = GetRandomMovieData()
#
# # For now just switch False - for get full random movie and True - for genre random movie
# # movie_data.get_movie_data(input("Жанры/Genres (через запятую): ").split(','), True)
# #
# # print("Movie Name:", movie_data.film_name)
# # print("Genre:", movie_data.film_genre)
# # print("Rating:", movie_data.film_rating_imb)
# # print("Description:", movie_data.film_desc)
