import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


user_input = input("Genre: ")


class ParsSettings:
    def __init__(self):
        self.url = "https://www.kinopoisk.ru/chance/"
        self.url_for_img = "https://www.kinopoisk.ru/"

        self.response = requests.get(self.url)
        self.driver = webdriver.Chrome()

        self.user_genre_key = None
        self.genres = {
            'genre_1750 ': 'Anime', 'genre_22 selectItem': 'biography',
            'genre_3 selectItem': 'action movie', 'genre_13 selectItem': 'Western',
            'genre_19 selectItem': 'Military', 'genre_17 selectItem': 'Detective',
            'genre_456 selectItem': 'Kids', 'genre_12 selectItem': 'documentary',
            'genre_8 selectItem': 'Drama', 'genre_23 selectItem': 'History',
            'genre_6 selectItem': 'Comedy', 'genre_15 selectItem': 'short film',
            'genre_16 selectItem': 'Crime', 'genre_7 selectItem': 'Melodrama',
            'genre_21 selectItem': 'Music', 'genre_14 selectItem': 'Cartoon',
            'genre_9 selectItem': 'Musical', 'genre_10 selectItem': 'Adventure',
            'genre_11 selectItem': 'Family', 'genre_24 selectItem': 'Sport',
            'genre_4 selectItem': 'Thriller', 'genre_1 selectItem': 'Horror',
            'genre_2 selectItem': 'Fantastic', 'genre_18 selectItem': 'Film-Noir',
            'genre_5 selectItem': 'Fantasy'
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
        for key in self.genres:
            if self.genres[key] == genre:
                self.user_genre_key = key
                print("User Input:", user_input)
                print("Genre Key: ", self.user_genre_key)
                return self.user_genre_key
        print("Жанр не найден")
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

        self.checkbox = self.driver.find_element(By.CLASS_NAME, self.user_genre_key)
        if self.checkbox:
            self.user_genre_key = self.user_genre_key
            self.checkbox.click()
            self.button.click()
            self.new_html = self.driver.page_source
            self.soup = BeautifulSoup(self.new_html, "lxml")
            self.driver.quit()
            return self.soup
        else:
            print("No Same Genre")
            return None

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
movie_data.get_full_rnd_movie_data(False)

print("Movie Name:", movie_data.film_name)
print("Genre:", movie_data.film_genre)
print("Rating:", movie_data.film_rating_imb)
print("Description:", movie_data.film_desc)