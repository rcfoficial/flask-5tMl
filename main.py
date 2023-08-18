from flask import Flask, jsonify, request
import os
from pymongo import MongoClient

app = Flask(__name__)

# Configurações para a conexão com o MongoDB
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
    # Utilizando o método sort para ordenar em ordem decrescente pelo campo '_id'
    for entry in collection.find({}, {
        "number_sim": 1,
        "from_de": 1,
        "content": 1,
        "country": 1,
        "flag": 1,
        "site": 1,
        "data_created": 1,
        "_id": 0
    }).sort("_id", -1):
        result.append(entry)

    # Encapsula os resultados em uma chave "data"
    response_data = {"data": result}
    return jsonify(response_data)


@app.route('/list_numbers/<number_sim>')
def list_numbers_by_number_sim(number_sim):
    result = []
    for entry in collection.find({"number_sim": number_sim}, {
        "number_sim": 1,
        "from_de": 1,
        "content": 1,
        "country": 1,
        "flag": 1,
        "site": 1,
        "data_created": 1,
        "_id": 0
    }).sort("_id", -1):
        result.append(entry)

    # Encapsula os resultados em uma chave "data"
    response_data = {"data": result}
    return jsonify(response_data)


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
