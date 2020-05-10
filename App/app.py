from flask import Flask
import requests


app = Flask(__name__)

@app.route('/')
def index():
    #circle = Cicle()
    pass

@app.route('/test')
def stats():
    pass