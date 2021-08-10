from flask import Response
from bson.json_util import dumps

def json_response(data):
    return Response(
        dumps(data),
        mimetype="application/json"
    )