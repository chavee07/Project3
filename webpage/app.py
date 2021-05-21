# import pandas as pd
import sqlite3
# from sqlalchemy.orm import Session
import pprint
from flask import Flask, request, render_template, jsonify, current_app
import json

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

                   
#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return render_template('index.html')


@app.route("/index")
def home():
    """List all available api routes."""
    return render_template('index.html')

@app.route("/landing")
def names():

    #################################################
    # Database Setup
    #################################################
    con = sqlite3.connect("../Data/project3.sqlite")

    db = con.cursor()

    # Convert list of tuples into normal list
    results = db.execute('Select * from df').fetchall()

    # return jsonify(result)

    # Create a dictionary from the row data and append to a list of all_passengers
    all_countries = []
    for country, con_code, score, gdp, social, health, freedom, generosity, corruption, alcohol, beer_servings, wine_servings, spirit_servings in results:
        countries_dict = {}
        countries_dict["Country"] = country
        countries_dict["Country Code"] = con_code
        countries_dict["Score"] = score
        countries_dict["GDP per capita"] = gdp
        countries_dict["Social support"] = social
        countries_dict["Health life expectancy"] = health
        countries_dict["Freedom to make life choices"] = freedom
        countries_dict["Generosity"] = generosity
        countries_dict["Perceptions of corruption"] = corruption
        countries_dict["Alcohol Consumption per Capita (liter)"] = alcohol
        countries_dict["beer_servings"] = beer_servings
        countries_dict["wine_servings"] = wine_servings
        countries_dict["spirit_servings"] = beer_servings
        all_countries.append(countries_dict)

    return jsonify(all_countries)

    
@app.route("/maps")
def maps():
    return render_template('maps.html')

@app.route("/bar")
def bar():
    return render_template('bar.html')

@app.route("/bubble")
def bubble():
    return render_template('bubble.html')

@app.route("/gauge")
def gauge():
    return render_template('gauge.html')



if __name__ == '__main__':
    app.run(debug=True)