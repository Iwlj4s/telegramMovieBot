import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time


user_input = input("Genre: ")


class ParsSettings:
    def __init__(self):
        self.url = "https://www.kinopoisk.ru/chance/"
        self.url_for_img = "https://www.kinopoisk.ru/"

        self.response = requests.get(self.url)
        self.driver = webdriver.Chrome()

        self.user_genre_key = None
        self.genres = {
            '1750 ': 'Anime', '22': 'Biography',
            '3': 'Action movie', '13': 'Western',
            '19': 'Military', '17': 'Detective',
            '456': 'Kids', '12': 'Documentary',
            '8': 'Drama', '23': 'History',
            '6': 'Comedy', '15': 'Short film',
            '16': 'Crime', '7': 'Melodrama',
            '21': 'Music', '14': 'Cartoon',
            '9 ': 'Musical', '10': 'Adventure',
            '11': 'Family', '24': 'Sport',
            '4': 'Thriller', '1': 'Horror',
            '2': 'Fantastic', '18': 'Film-Noir',
            '5': 'Fantasy'
        }


class GetRandomMovieData(ParsSettings):
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

        self.driver.get(self.url)

        self.list = self.driver.find_element(By.ID, "genreListTitle")
        self.button = self.driver.find_element(By.CLASS_NAME, "button")

        self.new_html = None
        self.soup = None

    def find_user_genre(self, genre):
        """
        dict genre: keys == class <li> in HTML || values == genres
        :return: genre key by user input genre, like: Anime: genre_1750
        """

        for key in self.genres:
            if self.genres[key] == genre:
                self.user_genre_key = key
                print("User Input:", user_input)
                print("Genre Key: ", self.user_genre_key)
                return self.user_genre_key
        print("No Same Gener")
        return None

    def get_rnd_movie(self):
        self.button.click()
        self.new_html = self.driver.page_source
        self.soup = BeautifulSoup(self.new_html, "lxml")
        self.driver.quit()
        return self.soup

    def get_rnd_gener_movie(self):
        self.find_user_genre(user_input)
        self.list.click()

        time.sleep(5)
        self.driver.find_element(By.XPATH, f"//input[@value='{self.user_genre_key}']").click()

        time.sleep(5)
        self.button.click()

        self.new_html = self.driver.page_source
        self.soup = BeautifulSoup(self.new_html, "lxml")

        self.driver.quit()
        return self.soup

    def get_full_rnd_movie_data(self, genre=False):
        self.soup = None

        if not genre:
            self.soup = self.get_rnd_movie()
        elif genre:
            self.soup = self.get_rnd_gener_movie()

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


movie_data = GetRandomMovieData()

# For now just switch False - for get full random movie and True - for genre random movie
movie_data.get_full_rnd_movie_data(True)

print("Movie Name:", movie_data.film_name)
print("Genre:", movie_data.film_genre)
print("Rating:", movie_data.film_rating_imb)
print("Description:", movie_data.film_desc)