import pika, sys, os


def main():
    url = os.environ.get('MESSAGE_BROKER_DSN', 'amqp://guest:guest@broker:5672/%2f')
    # print('broker url {}'.format(url))
    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()

    channel.queue_declare(queue='insert_single_result')

    channel.exchange_declare(exchange='insert_single_result', exchange_type='direct')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.queue_bind(queue='insert_single_result', exchange='insert_single_result',
                       routing_key='insert_single_result')
    channel.basic_consume(queue='insert_single_result', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
