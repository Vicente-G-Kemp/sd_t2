from confluent_kafka import Consumer, TopicPartition, KafkaError
import sqlite3

con = sqlite3.connect("huesillo.db")
cur = con.cursor()

cur.execute("""SELECT name FROM sqlite_master WHERE type='table';""")
print(cur.fetchall())

consumer_config = {
    'bootstrap.servers': 'PLAINTEXT://:9092', 
    'group.id': 'test-consumer-group',
    #'auto.offset.reset': 'earliest' 
}

consumer = Consumer(consumer_config)

topic = 'registros'
#consumer.subscribe([topic])

consumer.assign([TopicPartition('registros', 1)])
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
        data_list = str(msg.value().decode('utf-8')).split(",")
        print(data_list)
        print(data_list[0])
        cur.execute("INSERT INTO maestro (username, pass, email) VALUES (?, ?, ?)", (data_list[0], data_list[1], data_list[2]))
        con.commit()