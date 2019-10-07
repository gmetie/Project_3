# from .app import db

# import pandas as pd
# import json
# import requests
# import sqlalchemy
# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session
# from sqlalchemy import create_engine

# from .api_key import api_key

# lat = "40.0274"
# lon = "-105.2519"
# maxDistance = "1000"
# maxResults = "1000"

# api_url = f"https://www.hikingproject.com/data/get-trails?lat={lat}&lon={lon}9&maxDistance={maxDistance}&maxResults={maxResults}&key={api_key}"


# class hiking(db.Model):
#     __tablename__ = 'hiking'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64))
#     type = db.Column(db.String(64))
#     summary = db.Column(db.String(600))
#     difficulty = db.Column(db.String(64))
#     stars = db.Column(db.Float)
#     starVotes = db.Column(db.Integer)
#     location = db.Column(db.String(64))
#     url = db.Column(db.String(164))
#     imgSqSmall = db.Column(db.String(164))
#     imgSmall = db.Column(db.String(164))
#     imgSmallMed = db.Column(db.String(164))
#     imgMedium = db.Column(db.String(164))
#     length = db.Column(db.Float)
#     ascent = db.Column(db.Float)
#     descent = db.Column(db.Float)
#     high = db.Column(db.Float)
#     low = db.Column(db.Float)
#     longitude = db.Column(db.Float)
#     latitude = db.Column(db.Float)
#     conditionStatus = db.Column(db.String(64))
#     conditionDetails = db.Column(db.String(64))
#     conditionDate = db.Column(db.Float)


#     def __init__(self):
#         try:
#             response = requests.get(api_url)

#             response.raise_for_status()
#                 # Jsonify Responce
#             json_obj = response.json()
#                 # Create Pandas Dataframe
#             df = pd.DataFrame(json_obj['trails'])
#                 # Send Pandas Dataframe to DB
#             self.df.to_sql(name='hiking', con=engine, if_exists='replace', index=True)

#         except requests.exceptions.HTTPError as e:
#             # if error keep going
#             pass


    # def __init__(self, name, type, summary, difficulty, stars, starvotes, location, url, imgSqSmall, imgSmall, imgSmallMed, 
    # imgMedium,length, ascent,descent,high,low,longitude,latitude,conditionStatus,conditionDetails,conditionDate):
    #     self.name = name
    #     self.type = type
    #     self.summary = summary
    #     self.difficulty = difficulty
    #     self.stars = stars
    #     self.starVotes = starvotes
    #     self.location = location
    #     self.url = url
    #     self.imgSqSmall = imgSqSmall
    #     self.imgSmall = imgSmall 
    #     self.imgSmallMed = imgSmallMed
    #     self.imgMedium = imgMedium
    #     self.length = length
    #     self.ascent = ascent
    #     self.descent = descent
    #     self.high = high
    #     self.low = low
    #     self.longitude = longitude
    #     self.latitude = latitude
    #     self.conditionStatus = conditionStatus
    #     self.conditionDate = conditionDate
