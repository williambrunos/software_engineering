from modules.message_queue import MessageQueue
import base64

def decode_base64_message(base64_message):
    decoded_bytes = base64.b64decode(base64_message)
    decoded_message = decoded_bytes.decode('utf-8')
    return decoded_message

# Callback function to handle receeived messages
def callback(chanel, method, properties, body):
    base64_string_received = body.decode('utf-8')  
    decoded_message = decode_base64_message(base64_string_received)
    print(f'Received: {decoded_message}')

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
