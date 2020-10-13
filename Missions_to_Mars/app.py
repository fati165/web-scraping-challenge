
from flask import Flask, jsonify
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

import numpy as np
import datetime as dt
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")

def homepage(): 

    # Find data
    marsinfo = mongo.db.marsdata.find_one()

    # Return template and data
    return render_template("index.html", mars_=marsinfo)

@app.route("/scrape")
def scrape(): 
    marsinfo = mongo.db.marsdata
    # Run scrapped functions
    _mars = scrape_mars.mars_scrape()
    marsinfo.replace_one({}, _mars, upsert=True)
    return "Scraping Succefull"
    #return render_template("index.html", mars_=mars_scrape)

#refer pymongo activities

if __name__ == "__main__":
    app.run(debug=True)