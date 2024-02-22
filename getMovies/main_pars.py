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

        self.user_genre_key = None
        self.genres = {
            '1750': 'anime', '22': 'biography',
            '3': 'action movie', '13': 'western',
            '19': 'military', '17': 'detective',
            '456': 'kids', '12': 'documentary',
            '8': 'drama', '23': 'history',
            '6': 'comedy', '15': 'short film',
            '16': 'crime', '7': 'melodrama',
            '21': 'music', '14': 'cartoon',
            '9 ': 'musical', '10': 'adventure',
            '11': 'family', '24': 'sport',
            '4': 'thriller', '1': 'horror',
            '2': 'fantastic', '18': 'film-noir',
            '5': 'fantasy'
        }


class Driver(ParsSettings):
    def __init__(self):
        super().__init__()
        self.driver.get(self.url)

        self.list = self.driver.find_element(By.ID, "genreListTitle")
        self.button = self.driver.find_element(By.CLASS_NAME, "button")

        self.new_html = None
        self.soup = None

    def find_user_gener(self, genre):
        """

        :param genre: dict genre, keys == value in HTML || values == genres
        :return: genre key by user input genre, like: Anime: 1750
        """
        print("User input: ", genre)
        for key in self.genres:
            if self.genres[key] == genre:
                self.user_genre_key = key
                print("Genre Key: ", self.user_genre_key)
                return self.user_genre_key
        print("No Same Gener")
        return None

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

    def get_rnd_gener_movie(self, u_genre):
        """
        u_gener => find_user_gener(gener)
        :return new HTML page with movie
        """
        self.find_user_gener(u_genre)
        self.list.click()

        time.sleep(1.5)
        print(self.user_genre_key)
        self.driver.find_element(By.XPATH, f"//input[@value='{self.user_genre_key}']").click()

        time.sleep(2)
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

# For now just switch False - for get full random movie and True - for genre random movie
# movie_data.get_movie_data("Comedy", True)

# print("Movie Name:", movie_data.film_name)
# print("Genre:", movie_data.film_genre)
# print("Rating:", movie_data.film_rating_imb)
# print("Description:", movie_data.film_desc)
