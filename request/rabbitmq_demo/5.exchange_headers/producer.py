import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.33.6'))
channel = connection.channel()

exchange_type = "headers_ex"
channel.exchange_declare(exchange=exchange_type,
                         exchange_type='headers')

headers = {
    "key1": "value1",
    "key2": "value3"
}

for i in range(10):
    message = "data%d" % i
    channel.basic_publish(exchange=exchange_type,
                          routing_key='',
                          body=message,
                          properties=pika.BasicProperties(headers = headers)
                          )
    print(" [x] Sent %r:%r" % (headers, message))

connection.close()

if __name__ == '__main__':
    pass