#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pika
  
credentials = pika.PlainCredentials('test', 'test')
connection = pika.BlockingConnection(pika.ConnectionParameters('172.30.136.52',5672,'/',credentials))
channel = connection.channel()
channel.queue_declare(queue='name2', durable=True)
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    import time
    time.sleep(10)
    print('ok')
    ch.basic_ack(delivery_tag = method.delivery_tag)
channel.basic_consume(callback,
                      queue='name2',
                      no_ack=False)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
