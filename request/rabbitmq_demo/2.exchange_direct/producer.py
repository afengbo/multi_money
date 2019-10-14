import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.33.6'))

channel = connection.channel()

exchange_name = "direct_ex"
channel.exchange_declare(exchange=exchange_name,
                         exchange_type='direct')


routing_key = 'info'

for i in range(10):
    message = "data%d-%s"%(i,routing_key)
    channel.basic_publish(exchange=exchange_name,
                          routing_key=routing_key,
                          body=message)

    print(" [x] Sent %r:%r" % (routing_key, message))

connection.close()

if __name__ == '__main__':
    pass
