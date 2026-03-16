import os
from confluent_kafka import Consumer

BOOTSTRAP_SERVERS = os.getenv('BOOTSTRAP_SERVERS', 'localhost:9092')

CONFIG = {
    "bootstrap.servers": BOOTSTRAP_SERVERS,
    "group.id": "intel",
    "auto.offset.reset": "earliest"
        }



class KafkaConsumer:
    consumer = None 

    @classmethod
    def get_consumer(cls):
        if cls.consumer is None:
            cls.consumer = Consumer(CONFIG)
        return cls.consumer
