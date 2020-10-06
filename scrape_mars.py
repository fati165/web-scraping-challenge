from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

def init_browser(): 
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    return browser  
# Create dict for Mongo

mars = {}
def news_scrape():
    browser = init_browser()
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
    browser.quit()

    return mars


def image_scrape():
    
    browser = init_browser()

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    browser.find_by_id("full_image").click()
    browser.find_link_by_partial_text("more info").click()
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser') 

    soupimage= soup.select_one("ul li div.download_tiff p a")
    soupimage.get("href")
    browser.quit()

    return mars


def facts_scrape():
    browser = init_browser()
    url = 'https://space-facts.com/mars/'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    souphtml= soup.select("table")
    souphtml[0]

    tables = pd.read_html(url)
    mars=tables[0]

    mars.columns= ["x","y"]
    return mars.to_html()


image_scrape()