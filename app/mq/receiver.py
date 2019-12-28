import pika
from app.utils import trade_util
conn=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel=conn.channel()

res=channel.queue_declare(queue='',exclusive=True)

queue_name=res.method.queue

channel.queue_bind(exchange='host',queue=queue_name)

def call_back(ch,method,prop,body):
    trade_util.process_trade(body)

channel.basic_consume(queue=queue_name,auto_ack=True,on_message_callback=call_back)

channel.start_consuming()