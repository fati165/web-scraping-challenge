
from flask import Flask, jsonify
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

import numpy as np
import datetime as dt
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/craigslist_app"
mongo = PyMongo(app)

@app.route("/")

def homepage(): 

    # Find data
    mars_scrape = mongo.db.mars_scrape.find_one()

    # Return template and data
    return render_template("index.html", mars_scrape=mars_scrape)

@app.route("/scrape")
def scrape(): 

    # Run scrapped functions
    mars_scrape = mongo.db.mars_scrape.find_one()
    scrape.update({}, mars_scrape, upsert=True)
    #return redirect("http://localhost:5000/", code=302)

#refer pymongo activities




if __name__ == "__main__":
    app.run(debug=True)