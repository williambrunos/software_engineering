import pika

# Callback function to handle receeived messages
def callback(chanel, method, properties, body):
    print(f'Received: {body.decode()}')
    
# Estabilish a connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Create a message queue
channel.queue_declare(queue='example_queue')

# Start consuming messages
channel.basic_consume(queue='example_queue', on_message_callback=callback, auto_ack=True)

# Continuously listen for messages
print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()