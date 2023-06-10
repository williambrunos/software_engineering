import pika

# Estabilish a connection with RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Create a message queue
channel.queue_declare(queue='example_queue')

# Send a message
channel.basic_publish(exchange='', routing_key='example_queue', body='hello world!')


# Close the connection
channel.close()