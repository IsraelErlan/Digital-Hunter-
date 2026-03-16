from confluent_kafka import Producer

CONFIG = {"bootstrap.servers": "localhost:9092"}

class KafkaProducer:
    producer = None

    @classmethod
    def get_producer(cls):
        if cls.producer is None:
            cls.producer = Producer(CONFIG)
        return cls.producer

