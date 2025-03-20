from django.core.management.base import BaseCommand 
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Run all log status'

    def add_arguments(self, parser):
        parser.add_argument("name",type=str)

    def handle(self, *args, **options):
        # call_command('migrate', interactive=False)
        name = options["name"]
        print(f"hi the tool is running {name}")