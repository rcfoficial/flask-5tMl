from flask import Flask, jsonify
import os
from pymongo import MongoClient

app = Flask(__name__)

mongo_uri = "mongodb+srv://admin:XjSEusRMtcXF4CrG@cluster0.zjgcps2.mongodb.net/"
client = MongoClient(mongo_uri)
db = client["database_sms"]
collection = db["list_numbers"]


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


@app.route('/list_numbers')
def list_numbers():
    result = []
    for entry in collection.find({}, {
        "number_sim": 1,
        "from_de": 1,
        "content": 1,
        "country": 1,
        "flag": 1,
        "site": 1,
        "data_created": 1,
        "_id": 0
    }):
        result.append(entry)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
