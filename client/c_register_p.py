from threading import Thread
from master import master_routine
from confluent_kafka import Consumer, TopicPartition, KafkaError
import sqlite3
con = sqlite3.connect("huesillo.db")
cur = con.cursor()

consumer_config = {
    'bootstrap.servers': 'PLAINTEXT://:9092', 
    'group.id': 'test-consumer-group',
}

consumer = Consumer(consumer_config)

topic = 'registros'

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
        print(f"Received message: {msg.value()}")
        data_list = str(msg.value().decode('utf-8')).split(",")
        try:
            cur.execute("INSERT INTO maestro (username, pass, email) VALUES (?, ?, ?)", (data_list[0], data_list[1], data_list[2]))
            cur.execute("SELECT master_id FROM maestro WHERE email = (?)", (data_list[2],))
            result = cur.fetchone()
            cur.execute("INSERT INTO ventas(master_id, current_ventas, current_earnings) VALUES (?, ?, ?)",(int(result[0]), 0, 0))
            cur.execute("INSERT INTO stock(master_id, current_stock) VALUES (?, ?)",(int(result[0]), 0))
            con.commit()
            print(result[0])
        except:
            print("Registry Error (premium_register)")
        else:
            t_m = Thread(target=master_routine, args=(result))
            t_m.daemon = True
            t_m.start()