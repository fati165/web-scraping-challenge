from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time

def init_browser(): 
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    return browser  
# Create dict for Mongo

def news_scrape():
    browser = init_browser()
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    time.sleep(5)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    souptitle= soup.select_one("ul.item_list li.slide")

    news_title = souptitle.find("div", class_= "content_title").get_text()

    soupP= soup.select_one("ul.item_list li.slide")

    new_p= soupP.find("div", class_= "article_teaser_body").get_text()
    

    browser.quit()

    return news_title, new_p


def image_scrape():
    
    browser = init_browser()

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    browser.find_by_id("full_image").click()
    browser.find_link_by_partial_text("more info").click()
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser') 

    soupimage= soup.select_one("figure.lede a")
    soupimage.get("href")
    browser.quit()

    return f"https://www.jpl.nasa.gov{soupimage.get('href')}"


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

    browser.quit()

    return mars

def hemisphere_scrape():
    browser = init_browser()
    USGSurl= "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(USGSurl)

    USGSurl="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    hemisphere_url="https://astrogeology.usgs.gov"

    browser.visit(USGSurl)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    main = soup.find_all('div', class_='item')

    #make list for the img urls
    title=[]
    hem_img= []

    for m in main:
        title = m.find('h3').text
        
        #link to image
        url_linkImage = m.find('a')['href']
        
        #then add the moon url to the link for image to direct the path there
        img_url= hemisphere_url+url_linkImage
        
        #go to site, parse!
        browser.visit(img_url)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        
        #then scrape for the image inside the site and print
        img_original= soup.find('div',class_='downloads')
        hem_url=img_original.find('a')['href']
        print(hem_url)
        
        
        img_data=dict({'title':title, 'img_url':hem_url})
        hem_img.append(img_data)
    #no need to for loop because it will repeatedly show all 4, 4 times    
    print (hem_img)
    browser.quit()
    #return mars

def mars_scrape():
    mars_ = {"news_title":news_scrape()[0],
            "news_paragraph": news_scrape()[1],
            "image": image_scrape(),
            "facts": facts_scrape(),
             "hemisphere": hemisphere_scrape()
           }
    return mars_



mars_scrape()