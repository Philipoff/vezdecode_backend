import io
import json


def show_all():
    with io.open('pictures.json', 'r', encoding='utf-8-sig') as f:
        pictures = json.load(f)
    for picture in pictures:
        picture = pictures[picture]
        print("Link in vk: " + picture["vk_url"])
        print("Author: " + picture["author"])
        print("Likes: " + str(picture["likes"]))
        print()


functions = {
    "like": show_all()
}

var = functions["like"]
