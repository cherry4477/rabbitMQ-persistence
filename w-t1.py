# -*- coding: utf-8 -*-
#!/usr/bin/env python
import pika
credentials = pika.PlainCredentials('test', 'test')
connection = pika.BlockingConnection(pika.ConnectionParameters('172.30.136.52',5672,'/',credentials))
channel = connection.channel()
channel.queue_declare(queue='name2', durable=True)    #指定队列持久化
channel.basic_publish(exchange='',
                      routing_key='name2',
                      body='Hello World!',
                      properties=pika.BasicProperties(
                          delivery_mode=2,            #指定消息持久化
                      ))
print(" [x] Sent 'Hello World!'")
connection.close()
