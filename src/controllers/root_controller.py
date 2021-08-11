from werkzeug.utils import HTMLBuilder
from utils.json_response import json_response
from app import app
from flask import request

@app.route("/")
def init():
    return "Welcome to my Barcelona API"