import pika
from typing import Callable

class MessageQueue:
    """
    Represents a message queue built upon RabbitMQ
    
    Attributes:
        connection: connection between the host and RabbitMQ
        channel: channel for message based comunication between sender and receiver
    """
    def __init__(self):
        """
        Initializes the message queue object without default setup
        """
        self._connection = ''
        self._channel = ''

    def estabilish_rabbitmq_connection(self, host: str):
        """
        Estabilishes the connection between the host and the RabbitMQ
        
        Args:
            :param host (str): host name of the server wich RabbitMQ is deployed (can be 'localhost')
        
        Returns:
            None
        """
        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host))

    def create_rabbitmq_channel(self):
        """
        Create a communication channel between host and RabbitMQ, allowing to create message queues
        
        Args:
            None
        
        Returns:
            None
        """
        self._channel = self._connection.channel()

    def create_rabbitmq_queue(self, queue_name: str):
        """
        Creates a message queue for communication between sender and receiver
        
        Args:
            :param queue_name (str): name of the queue that'll be created
            
        Returns:
            None
        """
        self._channel.queue_declare(queue=queue_name)
        
    def send_message(self, exchange='', routing_key='', body=''):
        """
        Send a message for the receiver using a queue
        
        Args:
            :param exchange (str): specifies the name of the exchange to publish to, see more in: https://www.rabbitmq.com/amqp-0-9-1-reference.html#basic.publish
            :param routing_key (str): specifies the unique name of the queue to publish the message
            :param body (str): message to be published in the queue
        
        Returns:
            None
        """
        self._channel.basic_publish(exchange=exchange, routing_key=routing_key, body=body)
        
    def setup_consuming_configs(self, queue: str, call_back_function: Callable, auto_ack: bool):
        """
        Setup a receiver consumming config to let the server consume messages from a queue
        
        Args:
            :param queue (str): name of the queue that the server will be consuming messages
            :param call_back_function (Callable): callback function that handles the queue message published
            :param auto_ack (bool): claims the queue exclusively for the receiver when True
            
        Returns:
            None
        """
        self._channel.basic_consume(queue=queue, on_message_callback=call_back_function, auto_ack=auto_ack)
    
    def start_consuming(self):
        """
        Makes the receiver start cunsuming the queue, the call back function will be executed every time
        that a message is published in the queue
        
        Args:
            None
        
        Returns:
            None
        """
        self._channel.start_consuming()
        
    def close_channel(self):
        """
        Closes the channel of communication between host and RabbitMQ
        
        Args:
            None
        
        Returns:
            None
        """
        self._channel.close()