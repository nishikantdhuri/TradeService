import pika

conn= pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel=conn.channel()

channel.exchange_declare(exchange='host',durable=True,exchange_type='fanout')
a=object()
channel.basic_publish(exchange='host',routing_key='',body='hi',properties=pika.BasicProperties(delivery_mode=2))

conn.close()