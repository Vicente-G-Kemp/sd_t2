from confluent_kafka import Producer
import socket
import time
import random

producer_config = {
    'bootstrap.servers': 'PLAINTEXT://:9092',
    'client.id': socket.gethostname()
}

producer = Producer(producer_config)

# Produce a message to a Kafka topic
topic = 'topic0'
message_key = 'key'
message_value = 'Hello, Kafka!'
while True:
    t_venta=random.randint(5,7)
    producer.produce(topic, key=message_key, value=message_value)
    producer.flush()
    time.sleep(t_venta)