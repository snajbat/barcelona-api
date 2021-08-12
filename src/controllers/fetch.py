from app import app
from flask import request
from utils.conditions import group_query
from utils.json_response import json_response
from utils.mongo_connection import mongo_read
from utils.handle_error import handle_error
from utils.conditions import group_query

@app.get("/neighborhood/<neigh>")
@handle_error
def read_mongo_neig(neigh):
    q = dict(request.args)
    group_query(q)

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


@app.get("/district/<district>")
@handle_error
def read_mongo_dis(district):
    q = dict(request.args)
    group_query(q)

    p = {"_id":0}
    resp = list(mongo_read({"District_Name": district}, p, q=q))

    if district.isnumeric():
        district = int(district)
        if district not in range(1,11):
            raise ValueError("Enter a valid District Code")
        return json_response(list(mongo_read({"District_Code": district}, p, q=q)))
    if not resp:
        raise ValueError("District not found")
    return json_response(resp)