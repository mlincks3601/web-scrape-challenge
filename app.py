# Import Dependencies 
from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
import scrape_python
import os


# Hidden authetication file
#import config 

# Create an instance of Flask app
app = Flask(__name__)


# Use flask_pymongo to set up mongo connection locally 
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_info_app"
mongo = PyMongo(app)

# Create route that renders index.html template and finds documents from mongo
@app.route("/")
def home(): 

    # Find data
    mars_info = mongo.db.mars_info.find_one()

    # Return template and data
    return render_template("index.html", mars_info=mars_info)

# Route that will trigger scrape function
@app.route("/scrape")
def scrape(): 

    # Run scrapped functions
    mars_info = mongo.db.mars_info
    mars_data = scrape_python.mars_news_scrape()
    mars_data = scrape_python.mars_image_scrape()
    mars_f = scrape_python.mars_facts_scrape()
    mars_w = scrape_python.mars_weather_scrape()
    mars_data = scrape_python.mars_hem_scrape()
    mars_info.update({}, mars_data, upsert=True)

    return redirect("/", code=302)

if __name__ == "__main__": 
    app.run(debug= True)
