from modules.message_queue import MessageQueue

def main():
    # Creating a MessageQueue class
    message_queue = MessageQueue()
    
    # Estabilish a connection with RabbitMQ
    message_queue.estabilish_rabbitmq_connection(host='localhost')
    message_queue.create_rabbitmq_channel()

    # Create a message queue
    queue_name='example_queue'
    message_queue.create_rabbitmq_queue(queue_name=queue_name)

    # Send a message
    message_queue.send_message(exchange='', routing_key='example_queue', body='hello world!')

    # Close the connection
    message_queue.close_channel()
    
    
if __name__ == "__main__":
    main()