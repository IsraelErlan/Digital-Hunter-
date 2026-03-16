import pymongo
import os

MONGO_URI = os.getenv('MONGO_URI', "mongodb://localhost:27017/")

class Mongo:
    connection = None
    collection = None

    @classmethod
    def get_connection(cls):
        if cls.connection is None:
            cls.connection = pymongo.MongoClient(MONGO_URI)
        return cls.connection
    
    @classmethod
    def get_collection(cls):
        if cls.collection is None:
            connection = cls.get_connection()
            db = connection["Digital_Hunter"]
            cls.collection = db["target_bank"]
        return cls.collection

