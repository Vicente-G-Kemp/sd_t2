from confluent_kafka import Consumer, TopicPartition, KafkaError
import sqlite3

con = sqlite3.connect("huesillo.db")
cur = con.cursor()

consumer_config = {
    'bootstrap.servers': 'PLAINTEXT://:9092', 
    'group.id': 'test-consumer-group',
}

consumer = Consumer(consumer_config)

topic = 'g_stock'

consumer.assign([TopicPartition('g_stock', 0)])

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
        print(f"Received message (STOCK): {msg.value()}")
        data_list = str(msg.value().decode('utf-8')).split(",")
        print(data_list)
        try:
            cur.execute("UPDATE stock SET current_stock = ? WHERE master_id = ?", (int(data_list[1]), int(data_list[0]),))
            con.commit()
        except:
            print("Registry Error - stock")