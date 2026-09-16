from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
col = MongoClient("mongodb://db:27017/").mon_tp_db.visits

@app.route('/')
def hello():
    col.insert_one({"message": "visite"})
    return f"Hello, World! Connexion réussie à MongoDB. Visites : {col.count_documents({})}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)