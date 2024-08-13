import requests
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


class ParsSettings:
    def __init__(self):
        self.url = "https://www.kinopoisk.ru/chance/"  # main page
        self.url_for_img = "https://www.kinopoisk.ru/"  # url for get movie's poster img

        self.response = requests.get(self.url)
        self.driver = webdriver.Chrome()

        self.user_genre_key = []
        self.user_country_key = []

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

        self.countries_ru = {
            '2': 'россия', '1': 'сша',
            '13': 'ссср', '25': 'австралия',
            '41': 'бельгия', '11': 'великобритания',
            '3': 'германия', '18': 'германия (фрг)',
            '28': 'гонконг', '4': 'дания',
            '29': 'индия', '15': 'испания',
            '14': 'италия', '6': 'канада',
            '31': 'китай', '26': 'корея южная',
            '17': 'мексика', '8': 'франция',
            '5': 'швеция', '9': 'япония'

        }


class Driver(ParsSettings):
    def __init__(self):
        super().__init__()
        self.driver.get(self.url)

        self.genre_list = self.driver.find_element(By.ID, "genreListTitle")  # genre select list
        self.country_list = self.driver.find_element(By.ID, "countryListTitle")  # country select list

        self.button = self.driver.find_element(By.ID, "search")  # get movie button

        self.new_html = None  # new HTML page with movie
        self.soup = None  # soup object

    def find_user_gener(self, u_genres):
        """
        :param u_genres:
        :return: genre key by user input genre, like: Anime: 1750
        """
        print("User util:", u_genres)
        for genre in u_genres:
            genre = genre.strip()
            for key in self.genres_ru:
                if self.genres_ru[key] == genre:
                    self.user_genre_key.append(key)
        print("Genre Keys: ", self.user_genre_key)
        return self.user_genre_key

    def find_user_country(self, u_countries):
        """
        :param u_countries:
        :return: country key by user input country, like: USA: 1
        """

        print("User country: ", u_countries)

        for country in u_countries:
            country = country.strip()
            for key in self.countries_ru:
                if self.countries_ru[key] == country:
                    self.user_country_key.append(key)

        print("Countries Keys: ", self.user_country_key)
        return self.user_country_key

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

    def select_user_genre(self, u_genres):
        """
        :param u_genres: it's user genre like: ['Аниме', 'Боевик'].lower()
        It's select genre from select list 
        """
        self.find_user_gener(u_genres)
        self.genre_list.click()
        print(self.user_genre_key)
        for key in self.user_genre_key:
            li = "genre_" + key
            print("full genre li tag: ", li)
            self.driver.execute_script(f"document.querySelector('li.{li} label input[value=\"{key}\"]').click()")
            time.sleep(1)

        time.sleep(1)

    def select_user_country(self, u_country):
        """
        :param u_country: it's user country like: ['США', 'Франция'].lower()
        It's select country from select list
        """
        self.find_user_country(u_country)

        self.country_list.click()
        print(self.user_country_key)
        for key in self.user_country_key:
            li = "country_" + key
            print("full country li tag: ", li)
            self.driver.execute_script(f"document.querySelector('li.{li} label input[value=\"{key}\"]').click()")
            time.sleep(1)
        time.sleep(1)

    def get_rnd_gener_movie(self, u_genres, u_country):
        """
        u_gener => find_user_gener(gener)
        :return new HTML page with movie
        """

        # selecting user GENRE
        self.select_user_genre(u_genres=u_genres)

        time.sleep(2)

        # selecting user COUNTRY
        self.select_user_country(u_country=u_country)

        time.sleep(1)

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

    def get_movie_data(self, user_gener, user_country, genre=False):
        """
        :param user_country:
        :param user_gener:  => get_rnd_gener_movie(u_gener)
        :param genre: If false: get random movie with random genre Else: get random movie with selected genre
        :return: movie data
        """
        self.soup = None

        if not genre:
            self.soup = self.get_rnd_movie()
        elif genre:
            self.soup = self.get_rnd_gener_movie(user_gener, user_country)

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

# For now just switch False - for get full random movie and True - for genre random movie
# genres = input("Жанры/Genres (через запятую): ").split(',')
# countries = input("Страны (через запятую): ").split(',')
# movie_data.get_movie_data(user_gener=genres, user_country=countries, genre=True)
#
# print("Movie Name:", movie_data.film_name)
# print("Genre:", movie_data.film_genre)
# print("Rating:", movie_data.film_rating_imb)
# print("Description:", movie_data.film_desc)
