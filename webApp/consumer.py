import sys
import os
from tayara_stats.services import insert_result_consumer
from tayara_stats.message_handlers import handle_log


def main():
    insert_result_consumer.consume(callback=handle_log)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
