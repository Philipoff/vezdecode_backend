from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient(
    "mongodb://vcodebackend:vcodebackend@194.67.111.141:27017/vcodebackend?authSource=vcodebackend&readPreference"
    "=primary&directConnection=true&ssl=false")
settings_collecion = client["vcodebackend"]["settings"]
pictures_collecion = client["vcodebackend"]["pictures"]

current_settings = settings_collecion.find_one({"_id": ObjectId("62641e34bc8c11b07d116c1c")})

favorite_meme_picture_link = input("Enter a link to your favorite picture or skip to save current one")
if pictures_collecion.count_documents({"photo_url": favorite_meme_picture_link}) >= 1:
    pass
else:
    if favorite_meme_picture_link:
        print("Wrong link!")
    favorite_meme_picture_link = current_settings["favorite_meme_picture_link"]

chance_if_less = input("Enter the chance to show favorite picture if the number of likes on another picture is less "
                       "(probability between 0 and 1), or skip to save current chance")
if chance_if_less:
    try:
        0 <= float(chance_if_less) <= 1
    except Exception as e:
        chance_if_less = current_settings["chance_if_less"]
        print("Wrong value!")
else:
    chance_if_less = current_settings["chance_if_less"]

chance_if_more = input("Enter the chance to show favorite picture if the number of likes on another picture is "
                       "more (probability between 0 and 1), or skip to save current chance")

if chance_if_more:
    try:
        0 <= float(chance_if_more) <= 1
    except Exception as e:
        chance_if_more = current_settings["chance_if_more"]
        print("Wrong value!")
else:
    chance_if_more = current_settings["chance_if_more"]

distance_between_favorite = input("Enter a distance in pictures between favorite pictures or skip to save current one")

if distance_between_favorite:
    try:
        0 <= int(distance_between_favorite)
    except Exception as e:
        distance_between_favorite = current_settings["distance_between_favorite"]
        print("Wrong value!")
else:
    distance_between_favorite = current_settings["distance_between_favorite"]

access_key = input("Enter the access key for the dashboard or skip to save current one")
if not access_key:
    access_key = current_settings["access_key"]

settings_collecion.update_one({"_id": ObjectId("62641e34bc8c11b07d116c1c")},
                              {"$set": {
                                  "favorite_meme_picture_link": favorite_meme_picture_link,
                                  "chance_if_less": float(chance_if_less),
                                  "chance_if_more": float(chance_if_more),
                                  "distance_between_favorite": int(distance_between_favorite),
                                  "access_key": access_key
                              }})
