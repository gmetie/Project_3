# import necessary libraries
import os

import pandas as pd
import numpy as np

import requests
import json
# from .api_key import api_key

from sqlalchemy import create_engine

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)


app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db/hiking.sqlite"
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '')
db = SQLAlchemy(app)


api_key = "200602075-3dd15f21d86fec1206fac0fe2d9117c8"

lat = "40.0274"
lon = "-105.2519"
maxDistance = "1000"
maxResults = "1000"

api_url = f"https://www.hikingproject.com/data/get-trails?lat={lat}&lon={lon}9&maxDistance={maxDistance}&maxResults={maxResults}&key={api_key}"
# from .models import hiking



class Hiking(db.Model):
    __tablename__ = 'hiking'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    type = db.Column(db.String(64))
    summary = db.Column(db.String(600))
    difficulty = db.Column(db.String(64))
    stars = db.Column(db.Float)
    starVotes = db.Column(db.Integer)
    location = db.Column(db.String(64))
    url = db.Column(db.String(164))
    imgSqSmall = db.Column(db.String(164))
    imgSmall = db.Column(db.String(164))
    imgSmallMed = db.Column(db.String(164))
    imgMedium = db.Column(db.String(164))
    length = db.Column(db.Float)
    ascent = db.Column(db.Float)
    descent = db.Column(db.Float)
    high = db.Column(db.Float)
    low = db.Column(db.Float)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    conditionStatus = db.Column(db.String(64))
    conditionDetails = db.Column(db.String(64))
    conditionDate = db.Column(db.Float)

    def __repr__(self):
        return '<Hiking %r>' % (self.name)




@app.before_first_request
def setup():
    db.create_all()

# create route that renders index.html template
@app.route("/")
def home():
    response = requests.get(api_url)

    response.raise_for_status()
            # Jsonify Responce
    json_obj = response.json()
            # Create Pandas Dataframe
    df = pd.DataFrame(json_obj['trails'])

            # Send Pandas Dataframe to DB
    df.to_sql(name='hiking', con=db.engine, if_exists='replace', index=True)

    return render_template("index.html")

@app.route("/api/hiking")
def api_Hiking():
    results = db.session.query(Hiking.id, 
    Hiking.name, 
    Hiking.type, 
    Hiking.summary, 
    Hiking.difficulty, 
    Hiking.stars, 
    Hiking.starVotes, 
    Hiking.location, 
    Hiking.url, 
    Hiking.imgSqSmall,
    Hiking.imgSmall,
    Hiking.imgSmallMed,
    Hiking.imgMedium,
    Hiking.length,
    Hiking.ascent,
    Hiking.descent,
    Hiking.high,
    Hiking.low,
    Hiking.longitude,
    Hiking.latitude, 
    Hiking.conditionStatus,
    Hiking.conditionDetails, 
    Hiking.conditionDate).all()
    

    hiking_data = []
    for result in results:
        hiking_data.append({
        "id": result[0],
        "name": result[1],
        "type": result[2],
        "summary": result[3],
        "difficulty": result[4],
        "stars": result[5],
        "starVotes": result[6],
        "location": result[7],
        "url": result[8],
        "imgSqSmall": result[9],
        "imgSmall":result[10],
        "imgSmallMed": result[11],
        "imgMedium": result[12],
        "length": result[13],
        "ascent": result[14],
        "descent": result[15],
        "high": result[16],
        "low": result[17],
        "longitude": result[18],
        "latitude": result[19],
        "conditionStatus": result[20],
        "conditionDetails": result[21],
        "conditionDate": result[22]
        })

    return jsonify(hiking_data)

@app.route("/api/trails")
def api_Hiking1():
    results = db.session.query(Hiking.id, 
    Hiking.name, 
    Hiking.type, 
    Hiking.summary, 
    Hiking.difficulty, 
    Hiking.stars, 
    Hiking.starVotes, 
    Hiking.location, 
    Hiking.url, 
    Hiking.imgSqSmall,
    Hiking.imgSmall,
    Hiking.imgSmallMed,
    Hiking.imgMedium,
    Hiking.length,
    Hiking.ascent,
    Hiking.descent,
    Hiking.high,
    Hiking.low,
    Hiking.longitude,
    Hiking.latitude, 
    Hiking.conditionStatus,
    Hiking.conditionDetails, 
    Hiking.conditionDate).all()
    

    trail_data = []
    for result in results:
        trail_data.append({
        "id": result[0],
        "name": result[1],
        "type": result[2],
        "summary": result[3],
        "difficulty": result[4],
        "stars": result[5],
        "starVotes": result[6],
        "location": result[7],
        "url": result[8],
        "imgSqSmall": result[9],
        "imgSmall":result[10],
        "imgSmallMed": result[11],
        "imgMedium": result[12],
        "length": result[13],
        "ascent": result[14],
        "descent": result[15],
        "high": result[16],
        "low": result[17],
        "longitude": result[18],
        "latitude": result[19],
        "conditionStatus": result[20],
        "conditionDetails": result[21],
        "conditionDate": result[22]
        })

    return jsonify(trail_data)


# @app.route("/data")
# def return_json(database):
#     try:
#         response = requests.get(url)

#         response.raise_for_status()
#             # Jsonify Responce
#         json_obj = response.json()
#             # Create Pandas Dataframe
#         df = pd.DataFrame(json_obj['trails'])
#             # Send Pandas Dataframe to DB
#         df.to_sql(name='hiking', con=engine, if_exists='replace', index=True)

#         print('it worked?')
#     except requests.exceptions.HTTPError as e:
#         # if error keep going
#        pass
    
if __name__ == "__main__":
    app.run()
