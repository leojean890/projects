import stomp


# Define a listener to process incoming messages
class MessageListener(stomp.ConnectionListener):
    def on_message(self, frame):
        print(f"Received message: {frame.body}")


# Define the Consumer class to listen for messages
class Consumer:
    def __init__(self, broker_host, broker_port, queue_name):
        self.conn = stomp.Connection([(broker_host, broker_port)])
        self.queue_name = queue_name

    def connect(self):
        self.conn.set_listener('', MessageListener())
        self.conn.connect(wait=True)
        self.conn.subscribe(destination=f'/queue/{self.queue_name}', id=1, ack='auto')
        print(f"Subscribed to queue: {self.queue_name}")

    def disconnect(self):
        self.conn.disconnect()


if __name__ == "__main__":
    broker_host = "localhost"
    broker_port = 61613
    queue_name = "test-queue"

    consumer = Consumer(broker_host, broker_port, queue_name)
    consumer.connect()

    # Keep the consumer running to listen for messages
    input("Press Enter to stop the consumer...\n")

    consumer.disconnect()
