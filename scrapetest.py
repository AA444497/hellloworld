from selenium import webdriver
import time
web = 'https://sportsbook.draftkings.com/leagues/football/88670561?category=game-lines&subcategory=game' #you can choose any other league
path = '/Users/Arjuna/Downloads/chromedriver' #introduce your file's path inside '...'
driver = webdriver.Chrome(path)
driver.get(web)
