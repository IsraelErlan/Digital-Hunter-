from .connection import Mongo

def find_target(target):
    entity_id = target['entity_id']
    collection = Mongo.get_collection()
    last_target = collection.find_one({'entity_id': entity_id})

    if last_target: 
        collection.delete_one({'entity_id': entity_id}) # לא יעיל במקרה של שגיאות 

    return last_target
    


def save_target_to_mongo(target):
    collection = Mongo.get_collection()
    collection.insert_one(target)
    print('target saved')
    print(target)


