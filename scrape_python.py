from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd
import os
import time
import requests
import warnings
warnings.filterwarnings('ignore')

def initial_browser():
    # @NOTE: Path to my chromedriver
    executable_path = {"executable_path": "C:\\Users\\mlinc\\Appdata\\Local\\rasjani\\WebDriverManager\\bin\\chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

# Create a misson to mars dictionary that can be imported into Mongo
mars_info = {}

# scrape nasa mars news
def mars_news_scrape():

        # Initialize browser 
        browser = initial_browser()

        browser.is_element_present_by_css("div.content_title", wait_time=1)

        # Visit Nasa news url through splinter module
        url = 'https://mars.nasa.gov/news/'
        browser.visit(url)
        html = browser.html
        # Parse HTML with Beautiful Soup
        soup = bs(html, 'html.parser')

        # Retrieve the latest news title and news paragraph
        news_title = soup.find('div', class_='content_title').find('a').text
        news_pg = soup.find('div', class_='article_teaser_body').text

        # Dictionary entry from MARS NEWS
        mars_info['news_title'] = news_title
        mars_info['news_paragraph'] = news_pg

        return mars_info

        browser.quit()

# FEATURED IMAGE
def mars_image_scrape():
        browser = initial_browser()

    #browser.is_element_present_by_css("img.jpg", wait_time=1)
    #use splinter to nav to the url
        featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(featured_image_url)

    # HTML Object 
        image_html = browser.html
        soup = bs(image_html, 'html.parser')

    # Retrieve background image url from style tag 
        url_for_image  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]

        main_url = 'https://www.jpl.nasa.gov'

    # combine the website url with scrapped route
        url_for_image = main_url + url_for_image
        url_for_image 

        # Dictionary entry from FEATURED IMAGE
        mars_info['image_url'] = url_for_image 
        
        browser.quit()

        return mars_info

        

# Mars Weather 
def mars_weather_scrape():

        # Initialize browser 
        browser = initial_browser()

        #browser.is_element_present_by_css("div", wait_time=1)

        # Visit Mars Weather Twitter through splinter module
        weather_url = 'https://twitter.com/marswxreport?lang=en'
        browser.visit(weather_url)

        # HTML Object 
        html_weather = browser.html

        # Parse HTML with Beautiful Soup
        soup = bs(html_weather, 'html.parser')

        # Find all elements that contain tweets
        latest_tweets = soup.find_all('div', class_='js-tweet-text-container')

        # Retrieve all elements that contain news title in the specified range
        # Look for entries that display weather related words to exclude non weather related tweets 
        for tweet in the_latest_tweets: 
            mars_weather = tweet.find('p').text
            if 'Sol' and 'pressure' in mars_weather:
                break
            else: 
                pass
         # Dictionary entry from WEATHER TWEET
        mars_info['mars_weather'] = mars_weather

        browser.quit()

        return mars_info
        
# Mars Facts
def mars_facts_scrape():

# Initialize browser 
        browser = initial_browser()

# Visit Mars facts url 
        space_facts_url = 'http://space-facts.com/mars/'
        browser.visit(space_facts_url)

# Use Pandas to "read_html" to parse the URL
        mars_facts = pd.read_html(space_facts_url)

#Find Mars Facts DataFrame in the lists of DataFrames
        mars_facts_df = mars_facts[1]
#to give the unamed columns a name, rename them using "0"
        mars_facts_df = mars_facts[1]
        mars_facts_df.rename( columns={'Unnamed: 0':'new column name'}, inplace=True )
#drop the earth column from our dataframe
        mars_facts_df.drop(['Earth'], axis = 1) 

#now rename our columns
        new_mars_facts_df = mars_facts_df.drop(['Earth'], axis = 1)  

#rename our columns
        mars_facts_df_renamed = new_mars_facts_df.rename(columns = {"Mars - Earth Comparison":"Information"})

        # Dictionary entry from Mars Facts

        mars_info['mars facts'] = html_table

        return mars_info
# Save html code to folder Assets
        html_table = mars_facts_df_renamed.to_html()

# Strip unwanted newlines to clean up the table
        html_table.replace("\n", '')

# Save html code
        mars_facts_df_renamed.to_html("mars_facts_data.html")


def mars_hem_scrape():
        browser = initial_browser()

# Visit hemispheres website through splinter
        hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(hemispheres_url)

        html_hemispheres = browser.html
# Parse HTML with Beautiful Soup
        soup = bs(html_hemispheres, 'html.parser')
# Retreive all items that contain mars hemispheres info
        items = soup.find_all('div', class_='item')

# Create empty list for hemisphere urls 
        hem_url_list = []

# Store the main_ul 
        hem_main_url = 'https://astrogeology.usgs.gov' 

# Loop through the items store previously
        for i in items: 
            title = i.find('h3').text
            
# Then store the link that leads to full image website
            hem_img = i.find('a', class_='itemLink product-item')['href']
            
# Visit the link that contains the full image url 
            browser.visit(hemispheres_main_url + hem_img)
            
# HTML Object of individual hemisphere info website 
            hem_img = browser.html
            
# Parse the html with Beautiful Soup for every hemisphere info website 
            soup = bs( hem_img, 'html.parser')
            
# Retrieve full image source 
            img_url = hem_main_url + soup.find('img', class_='wide-image')['src']
            
# Add the retreived info into a list of dicts 
            hem_url_list.append({"title" : title, "img_url" : img_url})

        mars_info['hem url list'] = hem_url_list
        
       
        browser.quit()

        # Return mars_data dictionary 

        return mars_info