from utils.json_response import json_response
from app import app
from flask import request

@app.route("/")
def ejemplo():
    alumno = {
        "name":"pepe22"
    }
    return json_response(alumno)