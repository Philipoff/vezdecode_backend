from pymongo import MongoClient
from random import uniform

client = MongoClient(
    "mongodb://vcodebackend:vcodebackend@194.67.111.141:27017/vcodebackend?authSource=vcodebackend&readPreference"
    "=primary&directConnection=true&ssl=false")
pictures_collecion = client["vcodebackend"]["pictures"]
settings_collecion = client["vcodebackend"]["settings"]


def show_all():
    for picture in pictures_collecion.find():
        print("Link in browser: " + picture["photo_url"])
        print("Author: " + picture["author"])
        print("Likes: " + str(picture["likes"]))
        print()


def rate_pictures():
    config = settings_collecion.find_one()
    favorite_picture = pictures_collecion.find_one({"photo_url": config["favorite_meme_picture_link"]})
    chance_if_less = config["chance_if_less"]
    chance_if_more = config["chance_if_more"]
    distance_between_favorite = config["distance_between_favorite"]
    print("Rate the following memes...\n")
    not_a_favorite_in_a_row = distance_between_favorite + 1
    for picture in pictures_collecion.find():
        if picture["likes"] >= favorite_picture["likes"]:
            if uniform(0, 1) <= chance_if_more and not_a_favorite_in_a_row >= distance_between_favorite + 1:
                picture = favorite_picture
                not_a_favorite_in_a_row = 0
        else:
            if uniform(0, 1) <= chance_if_less and not_a_favorite_in_a_row >= distance_between_favorite + 1:
                picture = favorite_picture
                not_a_favorite_in_a_row = 0
        not_a_favorite_in_a_row += 1
        print("Link in browser: " + picture["photo_url"])
        print("Author: " + picture["author"])
        print("Likes: " + str(picture["likes"]))
        print()
        response = input("Like/Skip/Stop: \n").lower()
        if response == "like":
            pictures_collecion.update_one({"_id": picture["_id"]}, {"$inc": {"likes": 1}})
            print("Liked! Next meme...\n")
        elif response == "skip":
            print("Skipped. Next meme...\n")
            continue
        else:
            print("Stopped.\n")
            break


print("Hello!")
while True:
    response = input("What do you want to do? Rate/show all/close\n").lower()
    if response == "rate":
        rate_pictures()
    elif response == "show all":
        show_all()
    elif response == "close":
        print("Bye!")
        exit(0)
    else:
        print("Unknown command! Chose one of the following: Rate/show all/close")
