import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

url = "https://www.kinopoisk.ru/chance/"
url_for_img = "https://www.kinopoisk.ru/"

response = requests.get(url)

driver = webdriver.Chrome()
driver.get(url)

button = driver.find_element(By.CLASS_NAME, "button")
button.click()

new_html = driver.page_source
driver.quit()

# HTML after button pressed
soup = BeautifulSoup(new_html, "lxml")

# Get Movie Data
# Get Poster
poster_div = soup.find("div", class_="poster")
poster_img_href = poster_div.find("img")["src"]
poster_img = url_for_img + poster_img_href

# Get Film Name adn Genre
film_name_div = soup.find("div", class_="filmName")
film_name = film_name_div.find("a").text

film_genre_div = soup.find("div", class_="gray")
film_genre = film_genre_div.text.strip()

# Get Rating
film_rating_div = soup.find("div", class_="rating")
film_rating_imb = film_rating_div.text.strip()

# Get Description
film_desc_div = soup.find("div", class_="syn")
film_desc = film_desc_div.text.strip()

get_data = soup.find_all("div", class_="movieBlock _NO_HIGHLIGHT_")


print("Poster:", poster_img)
print("Name:", film_name)
print("Genre:", film_genre)
print("Rating:", film_rating_imb)
print("Description:", film_desc)