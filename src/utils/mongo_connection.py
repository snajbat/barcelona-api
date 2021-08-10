from pymongo import MongoClient

client = MongoClient()

def mongo_read(query={}, project=None, client=client):
    collection = client.get_database("bcn_data")["def_population"]
    return collection.find(query, project)

