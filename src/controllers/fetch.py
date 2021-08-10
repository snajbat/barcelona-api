from app import app
from flask import request
from utils.json_response import json_response
from utils.mongo_connection import mongo_read

@app.get("/search/<neigh>")
#@handle_error
def read_mongo(neigh):
    #q = dict(request.args)
    #print(q)
    if neigh.isnumeric():
        return json_response(list(mongo_read({"Neighborhood_Code": int(neigh)})))
    return json_response(list(mongo_read({"Neighborhooh_Name": neigh})))