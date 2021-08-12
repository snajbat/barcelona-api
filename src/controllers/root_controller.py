from werkzeug.utils import HTMLBuilder
from utils.json_response import json_response
from utils.mongo_connection import mongo_read
from app import app
from flask import request

@app.route("/")
def init():
    return json_response(list(mongo_read({}, {"_id":0})))