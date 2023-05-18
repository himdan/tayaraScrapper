import pika
import os


class Consumer:
    def __init__(self,
                 broker_dsn='',
                 queue='',
                 exchange='',
                 exchange_type='',
                 routing_key=''
                 ):
        self._broker_dsn = broker_dsn
        self._queue = queue
        self._exchange = exchange
        self._exchange_type = exchange_type
        self._routing_key = routing_key
        self._channel: pika.adapters.blocking_connection.BlockingChannel = None

    def consume(self, callback, auto_ack=True):
        self._start()
        self._consume(_callback=callback, auto_ack=auto_ack)

    def _start(self):
        params = pika.URLParameters(self._broker_dsn)
        connection = pika.BlockingConnection(params)
        self._channel = connection.channel()
        self._channel.queue_declare(queue=self._queue)
        self._channel.exchange_declare(exchange=self._exchange, exchange_type=self._exchange_type)
        self._channel.queue_bind(queue=self._queue, exchange=self._exchange, routing_key=self._routing_key)

    def _consume(self, _callback, auto_ack=True):
        self._channel.basic_consume(queue=self._queue, on_message_callback=_callback, auto_ack=auto_ack)
        self._channel.start_consuming()


insert_result_consumer = Consumer(
    broker_dsn=os.environ.get('MESSAGE_BROKER_DSN', 'amqp://guest:guest@broker:5672/%2f'),
    queue='insert_single_result',
    exchange='insert_single_result',
    exchange_type='direct',
    routing_key='insert_single_result'
)
