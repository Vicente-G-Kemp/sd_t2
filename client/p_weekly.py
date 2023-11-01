from confluent_kafka import Producer
import socket
import time

producer_config = {
    'bootstrap.servers': 'PLAINTEXT://:9092',
    'client.id': socket.gethostname()
}
producer = Producer(producer_config)

topic = 'weekly'
while True:
    time.sleep(20)
    print("Weekly Report!")
    producer.produce(topic, value="check")
    producer.flush()