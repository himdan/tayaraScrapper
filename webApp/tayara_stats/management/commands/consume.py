from django.core.management.base import BaseCommand, CommandError
from tayara_stats.message_handlers import handle_insert_result
from tayara_stats.services import insert_result_consumer


class Command(BaseCommand):
    help = "start consumer"

    def add_arguments(self, parser):
        parser.add_argument("queue", type=str)

    def handle(self, *args, **options):
        insert_result_consumer.consume(
            callback=handle_insert_result
        )
