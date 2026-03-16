from .connection import Mongo

def update_target(damage):
    entity_id = damage['entity_id']
    result = damage["result"]
    collection = Mongo.get_collection()
    query = { "entity_id": entity_id }
    value = { "$set": { "attaced.status": result } }
    collection.update_one(query, value)



