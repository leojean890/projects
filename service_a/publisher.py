import stomp
import time


# Define the Publisher class to send messages
class Publisher:
    def __init__(self, broker_host, broker_port, queue_name):
        self.conn = stomp.Connection([(broker_host, broker_port)])
        self.queue_name = queue_name

    def connect(self):
        self.conn.connect(wait=True)
        print(f"Connected to broker at {broker_host}:{broker_port}")

    def send_message(self, message):
        self.conn.send(destination=f'/queue/{self.queue_name}', body=message)
        print(f"Sent message: {message}")

    def disconnect(self):
        self.conn.disconnect()


if __name__ == "__main__":
    broker_host = "localhost"
    broker_port = 61613
    queue_name = "test-queue"

    publisher = Publisher(broker_host, broker_port, queue_name)
    publisher.connect()

    # Sending messages to the queue every 2 seconds
    for i in range(5):
        publisher.send_message(f"Test message {i + 1}")
        time.sleep(2)

    publisher.disconnect()
