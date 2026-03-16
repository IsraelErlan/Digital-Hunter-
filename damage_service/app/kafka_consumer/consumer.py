import json
from .connection import KafkaConsumer


consumer = KafkaConsumer.get_consumer()

consumer.subscribe(["damage"])

print("🟢 Consumer is running and subscribed to damage topic")

def get_damage()-> dict | None:
    try:
        msg = consumer.poll(1.0)
        if msg is None:
            return None
        if msg.error():
            print("❌ Error:", msg.error())
            return None

        value = msg.value().decode("utf-8")
        damage = json.loads(value)
        return damage
    except KeyboardInterrupt:
        print("\n🔴 Stopping consumer")


