import json
from .connection import KafkaProducer


producer = KafkaProducer.get_producer()

def delivery_report(err, msg):
    if err:
        print(f"❌ Delivery failed: {err}")
    else:
        print(f"✅ Delivered {msg.value().decode('utf-8')}")




def publish_event(msg):
    value = json.dumps(msg).encode("utf-8")
    producer.produce(
    topic="intel_signals_dlq",
    value=value,
    callback=delivery_report
                            )

    producer.flush()





