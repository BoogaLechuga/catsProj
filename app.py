from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")

def cats() :

    url = "https://api.thecatapi.com/v1/images/search?breed_ids=bamb"

    response = requests.get(url)

    json = response.json()

    url = json[0]["url"]

    return '<img src="' + url + '"> </img>'

