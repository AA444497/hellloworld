from selenium import webdriver
import time
web = 'https://sportsbook.draftkings.com/leagues/football/88670561?category=game-lines&subcategory=game' #you can choose any other league
path = '/Users/Arjuna/Downloads/chromedriver' #introduce your file's path inside '...'
driver = webdriver.Chrome(path)
driver.get(web)
teams = []
x12 = [] #3-way
odds_events = []

box = driver.find_element_by_xpath('sportsbook-league-page dkbetslip')

sport_title = box.find_elements_by_class_name('sportsbook-breadcrumb__end')

