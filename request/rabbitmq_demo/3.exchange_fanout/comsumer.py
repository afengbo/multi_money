import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.33.6'))

channel = connection.channel()

exchange_name = "fanout_ex"
channel.exchange_declare(exchange=exchange_name,
                         exchange_type='fanout')

result = channel.queue_declare(exclusive=True, queue='fanout2')
queue_name = result.method.queue

channel.queue_bind(exchange=exchange_name,
                   queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r" % body)


channel.basic_consume(on_message_callback=callback,
                      queue=queue_name,
                      auto_ack=True)

channel.start_consuming()

if __name__ == '__main__':
    pass