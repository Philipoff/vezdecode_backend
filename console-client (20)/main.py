from pymongo import MongoClient

client = MongoClient(
    "mongodb://vcodebackend:vcodebackend@194.67.111.141:27017/vcodebackend?authSource=vcodebackend&readPreference"
    "=primary&directConnection=true&ssl=false")
pictures_collecion = client["vcodebackend"]["pictures"]


def show_all():
    for picture in pictures_collecion.find():
        print("Link in browser: " + picture["photo_url"])
        print("Author: " + picture["author"])
        print("Likes: " + str(picture["likes"]))
        print()


def rate_pictures():
    print("Rate the following memes...\n")
    for picture in pictures_collecion.find():
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
