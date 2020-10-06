from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

def init_browser(): 
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

# Create dict for Mongo

mars = {}
def news_scrape():
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    souptitle= soup.select_one("ul.item_list li.slide")
    souptitle.find("div", class_= "content_title").get_text()
    news_title = souptitle.find("div", class_= "content_title").get_text()

    soupP= soup.select_one("ul.item_list li.slide")
    new_p= soupP.find("div", class_= "article_teaser_body").get_text()

    mars['news_title'] = news_title
    mars['new_p'] = new_p

    return mars

    browser.quit()