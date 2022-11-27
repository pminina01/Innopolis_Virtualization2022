import pika
import os

def consumer(user, password, host):
    credentials = pika.PlainCredentials(user, password)
    parameters = pika.ConnectionParameters(host=host, credentials=credentials)
    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()
    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(f"Received {body}")

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
    print('Waiting for messages')
    channel.start_consuming()

    connection.close()
