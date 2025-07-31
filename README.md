# Kinopoisk Random Movie Telegram Bot

This project is a Telegram bot that helps users discover random movies using data from the Kinopoisk website (www.kinopoisk.ru).

## Description

The bot combines a Kinopoisk parser with a Telegram interface, allowing users to easily get  random movies through a chat interface. It uses Selenium WebDriver and BeautifulSoup for web scraping, and Telegram bot library (aiogram) for the bot functionality.

You can check how it works on YouTube https://youtu.be/Y5h_AVFvHJw

I don't want to buy hosting for this project

## Important Note on Movie Selection

When users select multiple genres or countries, it's important to understand that Kinopoisk's random selection process works as follows:

- The website randomly selects ONE genre and/or ONE country from the user's input list.
- This means that if a user selects multiple genres (e.g., Horror and Thriller), the resulting movie might belong to only one of these genres (e.g., it could be just a Horror movie without Thriller elements).
- The same applies to country selection.

This behavior is inherent to Kinopoisk's system and not a limitation of the bot itself.

## Main Features

1. **Random Movie**
   - Users can request a completely random movie suggestion.


2. **Filtered Movie**
   - Users can specify genres and countries to get more targeted movie suggestions.


3. **Movie Information Display**
   For each suggested movie, the bot provides:
   - Movie title
   - Genre
   - IMDb rating
   - Brief description
   - Movie poster (if available)

## Components

1. **Kinopoisk Parser**
   - `ParsSettings`: Contains basic settings and dictionaries for genres and countries.
   - `Driver`: Manages Selenium WebDriver for web interactions.
   - `GetRandomMovieData`: Extracts and processes movie data from Kinopoisk.


2. **Telegram Bot Interface**
   - Implements an intuitive button-based interface for user interactions.
   - Handles user selections and processes requests.
   - Presents movie information in a user-friendly format.

## How It Works

1. Users start the bot and are presented with the main keyboard.
2. Based on the user's selection, the bot presents additional options or fetches a movie.
3. For genre or country selection, users can choose from predefined lists.
4. The bot uses the selections to query the Kinopoisk parser and return movie information

## Bot Interface Examples
<img width="1153" height="446" alt="image" src="https://github.com/user-attachments/assets/0bfbe3b1-386c-4099-af71-31ed2f0203bd" />


### 1. Random Movie Selection
<img width="1097" height="821" alt="image" src="https://github.com/user-attachments/assets/49dad3ff-f284-4256-a908-367fdccc3d60" />


### 2. Movie Selection with Chosen Genre (No Country Specified)

   * **Movie by genre button**
      <img width="847" height="182" alt="image" src="https://github.com/user-attachments/assets/4b0dd4ed-1988-4c31-af40-b66eee8bfc7a" />

   
   * **Choose genre/genres**
   <img width="1189" height="908" alt="image" src="https://github.com/user-attachments/assets/013d5d23-ce45-4693-b71c-29391b79e37d" />


   * **Do you want to choose one more genre? (We choose yes)(we skip it)**
   <img width="1077" height="764" alt="image" src="https://github.com/user-attachments/assets/b60d3c49-21c7-414e-82f8-ad0cb8b1b9d0" />


   * **Choose country/countries (we skip it)**
   
   <img width="1096" height="897" alt="image" src="https://github.com/user-attachments/assets/9535b209-29cf-416b-bea4-3f837c75c586" />

   
   * **Generate movie? (we choose yes)**
   <img width="1149" height="903" alt="image" src="https://github.com/user-attachments/assets/da92884b-4260-4816-be3a-a2db35ed3d0d" />


   * **Result**
   <img width="1165" height="830" alt="image" src="https://github.com/user-attachments/assets/35fe70c2-9f17-4a6f-b976-834bca26565a" />



### 3. Movie Selection with Chosen Genre and Country
   * **Movie by genre button**
      <img width="963" height="391" alt="image" src="https://github.com/user-attachments/assets/3a8c8fd4-fda8-40ed-aa8a-46db38d79470" />

   
   * **Choose genre/genres**
   <img width="907" height="487" alt="image" src="https://github.com/user-attachments/assets/abcc1996-d3ec-4065-a782-525e239a9558" />

   * **Do you want to choose one more genre? (We choose yes)**
   <img width="1033" height="661" alt="image" src="https://github.com/user-attachments/assets/67849c02-a0b2-4a8d-a802-273680c41608" />


   * **Choose country/countries**
   <img width="982" height="751" alt="image" src="https://github.com/user-attachments/assets/9afb62ae-70d4-4cb9-9e80-289a83565ca1" />

   * **Do you want to choose one more country? (We choose yes)**
   <img width="1033" height="661" alt="image" src="https://github.com/user-attachments/assets/67849c02-a0b2-4a8d-a802-273680c41608" />

   
   * **Generate movie? (we choose yes)**
<img width="1050" height="831" alt="image" src="https://github.com/user-attachments/assets/ad7efd65-967a-4385-b1f3-d2007c4d0e87" />


   * **Result**
   <img width="1050" height="831" alt="image" src="https://github.com/user-attachments/assets/7638435c-58e4-459f-967b-53ead08a28ba" />




