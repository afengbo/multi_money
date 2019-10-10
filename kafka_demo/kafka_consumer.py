from confluent_kafka import Consumer, KafkaError, TopicPartition


c = Consumer({
    'bootstrap.servers': '192.168.33.6:9092',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})

# tp = TopicPartition("mytopic", 1, 0)
# c.assign([tp])
# c.seek(tp)
c.subscribe(['mytopic'])

while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue

    print('Received message: {} - {} - {}'.format(msg.value().decode('utf-8'), msg.topic(), msg.partition()))

c.close()

if __name__ == '__main__':
    pass
