from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(
    "mongodb://vcodebackend:vcodebackend@194.67.111.141:27017/vcodebackend?authSource=vcodebackend&readPreference"
    "=primary&directConnection=true&ssl=false")
pictures_collecion = client["vcodebackend"]["pictures"]
settings_collecion = client["vcodebackend"]["settings"]


@app.route('/check_login_key', methods=["GET", "POST"])
def edit_new():
    config = settings_collecion.find_one()
    return jsonify({"access_key": config["access_key"]})


@app.get("/get_memes/<count>/<offset>")
def get_memes(count, offset):
    print(count, offset)
    memes = pictures_collecion.find({}, {"_id": 0}).skip(int(offset)).limit(int(count))
    return jsonify(memes)


@app.get("/get_top_meme")
def get_top_meme():
    meme = pictures_collecion.find({}).sort("likes", -1).limit(1)[0]
    meme["_id"] = 0
    return jsonify(meme)


@app.get("/get_total_likes")
def get_total_likes():
    likes_sum = sum([i["likes"] for i in pictures_collecion.find()])
    return jsonify({"likes_sum": likes_sum})


@app.get("/get_total_memes")
def get_total_memes():
    total_memes = pictures_collecion.count_documents({})
    return jsonify({"total_memes": total_memes})


@app.get("/get_graded_memes")
def get_graded_memes():
    graded_memes = pictures_collecion.count_documents({"likes": {"$gt": 0}})
    return jsonify({"graded_memes": graded_memes})


if __name__ == "__main__":
    app.run()
