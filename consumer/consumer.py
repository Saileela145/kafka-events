from confluent_kafka import Consumer
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
    'sasl.password': password,
    'group.id': 'analytics-group',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(conf)
consumer.subscribe([topic])

print("Waiting for messages...")
count=0
while count<5:
    msg = consumer.poll(1.0)
    if msg:
        print("Consumed:", json.loads(msg.value().decode('utf-8')))
        count+=1