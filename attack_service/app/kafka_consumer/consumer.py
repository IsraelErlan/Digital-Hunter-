import json
from .connection import KafkaConsumer


consumer = KafkaConsumer.get_consumer()

consumer.subscribe(["attack"])

print("🟢 Consumer is running and subscribed to attack topic")

def get_attack()-> dict | None:
    try:
        msg = consumer.poll(1.0)
        if msg is None:
            return None
        if msg.error():
            print("❌ Error:", msg.error())
            return None

        value = msg.value().decode("utf-8")
        attack = json.loads(value)
        return attack
    except KeyboardInterrupt:
        print("\n🔴 Stopping consumer")


