from confluent_kafka import Consumer, TopicPartition, KafkaError
import sqlite3

con = sqlite3.connect("huesillo.db")
cur = con.cursor()

consumer_config = {
    'bootstrap.servers': 'PLAINTEXT://:9092', 
    'group.id': 'test-consumer-group',
    #'auto.offset.reset': 'earliest' 
}

consumer = Consumer(consumer_config)

topic = 'registros'
#consumer.subscribe([topic])

consumer.assign([TopicPartition('registros', 0)])
while True:
    msg = consumer.poll(1.0) 

    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            print("Reached end of partition")
        else:
            print(f"Error: {msg.error()}")
    else:
        print(f"Received message: {msg.key()}: {msg.value()}")


consumer.close()