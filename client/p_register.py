from confluent_kafka import Producer
from confluent_kafka.admin import AdminClient
import socket
import time
producer_config = {
    'bootstrap.servers': 'PLAINTEXT://:9092, PLAINTEXT://:9093',
    'client.id': socket.gethostname(),
}
    

producer = Producer(producer_config)
topic = 'registros'

def p_type(is_paid, message):
    producer.produce(topic, partition=is_paid, value=message)
    producer.flush()