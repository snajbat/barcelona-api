from app import app
from flask import request
from utils.json_response import json_response
from utils.mongo_connection import mongo_read
from utils.handle_error import handle_error

@app.get("/search/<neigh>")
@handle_error
def read_mongo(neigh):
    q = dict(request.args)
    if q:
        if len(q)>2 or ("group" not in q.keys()):
            raise ValueError("You can only use the group query")
        if q["group"] not in ["gender","total","age"]:
            raise ValueError("Insert a valid group query: age, gender or total")

    p = {"_id":0}
    resp = list(mongo_read({"Neighborhood_Name": neigh}, p, q=q))

    if neigh.isnumeric():
        neigh = int(neigh)
        if neigh not in range(1,74):
            raise ValueError("Enter a valid Neighborhood Code")
        return json_response(list(mongo_read({"Neighborhood_Code": neigh}, p, q=q)))
    if not resp:
        raise ValueError("Neighborhood not found")
    return json_response(resp)