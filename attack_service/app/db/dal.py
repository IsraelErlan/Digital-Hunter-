from .connection import Mongo

def update_target(attack):
    entity_id = attack['entity_id']
    collection = Mongo.get_collection()
    query = { "entity_id": entity_id }
    value = { "$set": { "attaced": True } }
    collection.update_one(query, value)




