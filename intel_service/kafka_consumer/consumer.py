import json
import os

from confluent_kafka import Consumer

BOOTSTRAP_SERVERS = os.getenv('BOOTSTRAP_SERVERS', 'localhost:9092')

consumer_config = {
    "bootstrap.servers": BOOTSTRAP_SERVERS,
    "group.id": "intel",
    "auto.offset.reset": "earliest"
}


consumer = Consumer(consumer_config)

consumer.subscribe(["intel"])

print("🟢 Consumer is running and subscribed to orders topic")

def get_intel_msg()-> dict | None:
    try:
        msg = consumer.poll(1.0)
        if msg is None:
            return None
        if msg.error():
            print("❌ Error:", msg.error())
            return None

        value = msg.value().decode("utf-8")
        intel_msg = json.loads(value)
        return intel_msg
    except KeyboardInterrupt:
        print("\n🔴 Stopping consumer")


