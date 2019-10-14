import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.33.6'))
channel = connection.channel()

queue_name = "queue"
channel.queue_declare(queue=queue_name)

print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    print(" [x] Done")


channel.basic_consume(on_message_callback=callback,
                      queue=queue_name,
                      auto_ack=True)

channel.start_consuming()

if __name__ == '__main__':
    pass
