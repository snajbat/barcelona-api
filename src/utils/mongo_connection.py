from typing import Collection
from pymongo import MongoClient
from config import mongo_url

client = MongoClient(mongo_url)

def mongo_read(query={}, project=None, client=client, q=None):
    collection = client.get_database("bcn_data")["population"]
    if not q:
        return collection.find(query, project)

    cur = collection.aggregate([
            {"$match": query,},
            {
                "$group": {
                    "_id": {
                        "Neighborhood_Name": "$Neighborhood_Name",
                        "Gender": "$Gender" if "gender" in q.values() else None,
                        "Age": "$Age" if "age" in q.values() else None,
                        "District_Code": "$District_Code",
                        "District_Name": "$District_Name",
                        "Neighborhood_Code": "$Neighborhood_Code",
                        "location": "$location"
                    },
                    "Number": {"$sum": "$Number"}
                }
            }
        ])
    cur = list(cur)
    final_list = []
    for dictio in cur:
        dic = {key:value for key,value in dictio["_id"].items() if value}
        dic["Number"] = dictio["Number"]
        final_list.append(dic)
    
    return final_list