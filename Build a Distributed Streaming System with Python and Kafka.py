from confluent_kafka import Producer

def produce_messages(bootstrap_servers, topic):
    p = Producer({'bootstrap.servers': bootstrap_servers})

    # Produce messages
    for i in range(10):
        p.produce(topic, f"Message {i}".encode('utf-8'))
        p.flush()

    p.close()

bootstrap_servers = 'localhost:9092'
topic = 'my_topic'
produce_messages(bootstrap_servers, topic)

#4.Comsumer code:
from confluent_kafka import Consumer

def consume_messages(bootstrap_servers, topic):
    c = Consumer({'bootstrap.servers': bootstrap_servers, 'group.id': 'my_group', 'auto.offset.reset': 'earliest'})
    c.subscribe([topic])

    # Consume messages
    while True:
        msg = c.poll(1.0)

        if msg is None:
            continue

        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue

        print(f"Received message: {msg.value().decode('utf-8')}")

    c.close()

consume_messages(bootstrap_servers, topic)