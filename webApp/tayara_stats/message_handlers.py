def handle_log(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())


def handle_insert_result(ch, method, properties, body):
    pass
