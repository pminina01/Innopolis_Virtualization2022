import os

import pika

credentials = pika.PlainCredentials(os.getenv("USER"), os.getenv("PASSWORD"))
parameters = pika.ConnectionParameters(host=os.getenv('HOST'), credentials=credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print("Message sent to queue")
connection.close()
