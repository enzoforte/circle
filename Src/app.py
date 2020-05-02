from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"

@app.route('/covid/stats')
def stats():

    url = "https://covid-193.p.rapidapi.com/statistics"

    querystring = {"country":"italy"}

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "7c58847555mshbfa8d8a06d2cfb1p138208jsncf4c82087ba7"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.text