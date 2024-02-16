import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By


class parsSettings():
    def __init__(self):
        self.url = "https://www.kinopoisk.ru/chance/"
        self.url_for_img = "https://www.kinopoisk.ru/"

        self.response = requests.get(self.url)

        self.driver = webdriver.Chrome()


class getRandomMovieData(parsSettings):
    def __init__(self):
        super().__init__()

        # Movie Data #
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

        # Create Driver #
        self.driver.get(self.url)

        # Find "Generate Movie" Button and click on here #
        self.button = self.driver.find_element(By.CLASS_NAME, "button")
        self.button.click()

        # Create BS4 Object for new HTML after pressed button #
        self.new_html = self.driver.page_source
        self.driver.quit()

        # HTML after button pressed
        self.soup = BeautifulSoup(self.new_html, "lxml")

    def get_full_rnd_movie_data(self):
        # Get Movie Data
        # Get Poster
        self.poster_div = self.soup.find("div", class_="poster")
        self.poster_img_href = self.poster_div.find("img")["src"]
        self.poster_img = self.url_for_img + self.poster_img_href

        # Get Film Name adn Genre
        self.film_name_div = self.soup.find("div", class_="filmName")
        self.film_name = self.film_name_div.find("a").text

        self.film_genre_div = self.soup.find("div", class_="gray")
        self.film_genre = self.film_genre_div.text.strip()

        # Get Rating
        self.film_rating_div = self.soup.find("div", class_="rating")
        self.film_rating_imb = self.film_rating_div.text.strip()

        # Get Description
        self.film_desc_div = self.soup.find("div", class_="syn")
        self.film_desc = self.film_desc_div.text.strip()


