from confluent_kafka import Producer
from confluent_kafka.admin import AdminClient
import socket
import time

kafka_broker = {'bootstrap.servers': 'PLAINTEXT://:9092'}
producer_config = {
    'bootstrap.servers': 'PLAINTEXT://:9092, PLAINTEXT://:9093',
    'client.id': socket.gethostname(),
}

producer = Producer(producer_config)

topic = 'weekly'
while True:
    time.sleep(20)
    print("Weekly Report!")
    producer.produce(topic, value="check")
    producer.flush()