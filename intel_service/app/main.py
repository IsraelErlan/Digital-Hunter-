from kafka_consumer.consumer import get_intel_msg
from validation.validation import validate_error
from kafka_producer.producer import publish_event
from db.dal import save_target_to_mongo, find_target
from logic.haversine import haversine_km


# 
def calculate_distance_and_level(target, last_target):
    if not last_target:
        target['priority_level'] = 99
        target['movement_distance'] = 0
        save_target_to_mongo(target)

    else:
        lat1, lon1 = target['lat'], target['lon']
        lat2, lon2 = last_target['lat'], last_target['lon']
        target['movement_distance'] = haversine_km(lat1, lon1, lat2, lon2)
        save_target_to_mongo(target)

    


def handle_target_error(target, msg_error):
    target['reason'] = msg_error
    publish_event(target)


def main():
    while True:
        try:
            target = get_intel_msg()
            if not target: 
                continue 

            #add
            msg_error = validate_error(target)
            if msg_error: 
                handle_target_error(target, msg_error)
                continue

            last_target = find_target(target)
            
            target = calculate_distance_and_level(target, last_target)

            save_target_to_mongo(target)

        except Exception as e:
             print(str(e))

if __name__ == '__main__':
     main()







    
