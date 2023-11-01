from confluent_kafka import Producer
import socket
import random
import time
# This script IS a producer.


# There's two possible, logical, ways I recon this could be done. 
# The most obvious way would be to send a message for each sale to the sale-consumer and 
# then another each x sales to the stock-consumer.
# The other way, that would be more realistic in my eyes, and resource efficient too would be to store in this script x sales and then send
# both messages to their respective consumers, something like a local registry thats updated in longer intervals to the database.
# In syntesis, Option A: send a message for each loop and another each x loops. Option B: Send both messages each x loops.

def master_routine(master_id):

    producer_config = {
    'bootstrap.servers': 'PLAINTEXT://:9092',
    'client.id': socket.gethostname()
    }
    producer = Producer(producer_config)

    topic = 'r_ventas'
    topic1 = 'g_stock'

    precios = (100, 200, 300)
    # default_stock_limit = random.randint(8, 16)
    default_stock_limit = 3
    sales = 0
    moneh = 0

    while True:
        w_time = random.randint(1,2)
        time.sleep(w_time)
        sales += 1
        moneh += precios[random.randint(0,2)]

        if sales == default_stock_limit:
            producer.produce(topic, value=str(master_id)+","+str(sales)+","+str(moneh))
            producer.produce(topic1, value=str(master_id)+","+str(sales))
            producer.flush()
            sales = 0
            moneh = 0