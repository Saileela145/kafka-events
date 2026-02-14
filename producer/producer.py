from confluent_kafka import Producer
import time
import json
bootstrap_servers = "d5hrmat3g3kbe68ve3gg.any.us-east-1.mpx.prd.cloud.redpanda.com:9092"
username = "producer"
password = "kafka1234"
topic = "user-events"

conf = {
    'bootstrap.servers': bootstrap_servers,
    'security.protocol': 'SASL_SSL',
    'sasl.mechanism': 'SCRAM-SHA-256',
    'sasl.username': username,
    'sasl.password': password
}

producer = Producer(conf)

for i in range(5):
    event = {
        "event_id": i,
        "user": f"user_{i}",
        "action": "click",
        "timestamp": time.time()
    }
    producer.produce(topic, json.dumps(event).encode('utf-8'))
    print("Produced:", event)
    producer.flush()
    time.sleep(1)
from confluent_kafka import Producer
import time
import json

bootstrap_servers = "d5hrmat3g3kbe68ve3gg.any.us-east-1.mpx.prd.cloud.redpanda.com:9092"
username = "producer"
password = "<YOUR_PASSWORD>"
topic = "user-events"

conf = {
    'bootstrap.servers': bootstrap_servers,
    'security.protocol': 'SASL_SSL',
    'sasl.mechanism': 'SCRAM-SHA-256',
    'sasl.username': username,
    'sasl.password': password
}

producer = Producer(conf)

for i in range(5):
    event = {
        "event_id": i,
        "user": f"user_{i}",
        "action": "click",
        "timestamp": time.time()
    }
    producer.produce(topic, json.dumps(event).encode('utf-8'))
    print("Produced:", event)
    producer.flush()
    print("Done")
