from confluent_kafka import Consumer, TopicPartition, KafkaError
import sqlite3

con = sqlite3.connect("huesillo.db")
cur = con.cursor()

consumer_config = {
    'bootstrap.servers': 'PLAINTEXT://:9092', 
    'group.id': 'test-consumer-group',
}

consumer = Consumer(consumer_config)
consumer1 = Consumer(consumer_config)
# consumer.assign([TopicPartition('r_ventas', 0)])
consumer1.assign([TopicPartition('weekly', 0)])
consumer.assign([TopicPartition('r_ventas', 0)])

while True:
    msg = consumer.poll(1.0) 
    msg1 = consumer1.poll(1.0)

    if msg is None:
        continue
    else:
        print(f"Received message (SALES): {msg.value()}")
        data_list = str(msg.value().decode('utf-8')).split(",")
        print(data_list)
        try:
            cur.execute("UPDATE ventas SET current_ventas = ?, current_earnings = ? WHERE master_id = ?", (int(data_list[1]), int(data_list[2]), int(data_list[0]),))
            con.commit()
        except:
            print("Registry Error - sales")

    if msg1 is None:
        continue
    else:
        print("received")
        cur.execute("SELECT * FROM ventas")
        print(cur.fetchall())
        con.commit()