from kafka_consumer.consumer import get_attack
from db.dal import update_target


def main():
    while True:
        try:
            attack = get_attack()
            if attack: 
                update_target(attack)

        except Exception as e: 
            print(str(e))