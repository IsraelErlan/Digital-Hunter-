from kafka_consumer.consumer import get_attack
from db.dal import update_target
from logger import log_event



def main():
    while True:
        try:
            attack = get_attack()
            if attack: 
                update_target(attack)

        except Exception as e: 
            print(str(e))



if __name__ == '__main__':
     main()