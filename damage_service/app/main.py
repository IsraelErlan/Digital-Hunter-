from kafka_consumer.consumer import get_damage
from db.dal import update_target


def main():
    while True:
        try:
            damage = get_damage()
            if damage: 
                update_target(damage)

        except Exception as e: 
            print(str(e))