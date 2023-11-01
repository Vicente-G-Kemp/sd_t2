from confluent_kafka import Producer
import socket

producer_config = {
    'bootstrap.servers': 'PLAINTEXT://:9092',
    'client.id': socket.gethostname()
}
producer = Producer(producer_config)
topic = 'registros'

def p_type(is_paid, message):
    producer.produce(topic, partition=is_paid, value=message)
    producer.flush()