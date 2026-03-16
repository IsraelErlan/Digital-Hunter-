import pymongo
import os

MONGO_URI = os.getenv('MONGO_URI', "mongodb://localhost:27017/")

myclient = pymongo.MongoClient(MONGO_URI)

mydb = myclient["Digital Hunter"]

mycol = mydb["target bank"]

def get_collection():
    return mycol