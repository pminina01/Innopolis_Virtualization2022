import os
import pika

def producer(user, password, host):
    credentials = pika.PlainCredentials(user, password)
    parameters = pika.ConnectionParameters(host=host, credentials=credentials)
    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
    print("Message sent to queue")
    connection.close()
