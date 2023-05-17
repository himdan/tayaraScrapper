import os
import pika
import json

class Messenger:
  def __init__(self, exchange, routing_key):
    url = os.environ.get('MESSAGE_BROKER_DSN', 'amqp://guest:guest@broker:5672/%2f')
    # print('broker url {}'.format(url))
    params = pika.URLParameters(url)
    self.__exchange = exchange
    self.__routing_key = routing_key
    # print('routing key {} exchange {}'.format(exchange, routing_key))
    self.__connection = pika.BlockingConnection(params)
    self.__channel = self.__connection.channel()
    self.__channel.queue_declare(queue=exchange)
    self.__channel.exchange_declare(exchange=exchange,exchange_type='direct')

  def send(self, message):
    self.__channel.basic_publish(exchange=self.__exchange, routing_key=self.__routing_key, body=json.dumps(message))


result_topic = Messenger(exchange='insert_single_result', routing_key='insert_single_result')
