from modules.message_queue import MessageQueue
import json
import base64

def load_json_to_dict(path: str):
    with open(path) as file:
        return json.load(file)
    
def encode_string_to_base64(string: str, encoding='utf-8'):
    return base64.b64encode(string.encode(encoding)).decode(encoding)

def main():
    # Creating a MessageQueue class
    message_queue = MessageQueue()
    
    # Estabilish a connection with RabbitMQ
    message_queue.estabilish_rabbitmq_connection(host='localhost')
    message_queue.create_rabbitmq_channel()

    # Create a message queue
    queue_name='example_queue'
    message_queue.create_rabbitmq_queue(queue_name=queue_name)

    # Loading data
    dict_data = load_json_to_dict('./data/loan_data.json')

    # Converting dict to string
    string_data = json.dumps(dict_data)
    
    # Encoding the string to base64 message
    base64_data = encode_string_to_base64(string=string_data, encoding='utf-8')
    print(base64_data, type(base64_data))
    
    # Send a message
    message_queue.send_message(exchange='', routing_key='example_queue', body=base64_data)
    print('mensagem enviada!')

    # Close the connection
    message_queue.close_channel()
    
    
if __name__ == "__main__":
    main()