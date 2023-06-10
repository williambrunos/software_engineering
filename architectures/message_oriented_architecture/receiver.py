from modules.message_queue import MessageQueue

# Callback function to handle receeived messages
def callback(chanel, method, properties, body):
    print(f'Received: {body.decode()}')

def main():
    message_queue = MessageQueue()
    
    # Estabilish a connection to RabbitMQ
    message_queue.estabilish_rabbitmq_connection(host='localhost')
    message_queue.create_rabbitmq_channel()

    # Create a message queue
    queue_name='example_queue'
    message_queue.create_rabbitmq_queue(queue_name=queue_name)

    # Start consuming messages
    message_queue.setup_consuming_configs(queue='example_queue', call_back_function=callback, auto_ack=True)

    # Continuously listen for messages
    print('Waiting for messages. To exit press CTRL+C')
    try:
        message_queue.start_consuming()
    except KeyboardInterrupt:
        print('Quiting, thanks for using our software!')
    
    
if __name__ == '__main__':
    main()
