from usgsflows.admin import update_levels
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        update_levels()
