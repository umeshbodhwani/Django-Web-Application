#this file is for importing the squirrel data

from django.core.management.base import BaseCommand
from distutils.util import strtobool
from squirrel_tracker.models import Squirrel
import csv

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        Squirrel.objects.all().delete()
        with open(options['csv_file']) as f:
            reader = csv.DictReader(f)
            sq_data = list(reader)

        for item in sq_data:
            s = Squirrel(
                X=item['X'],
                Y=item['Y'],
                Shift=item['Shift'],
                Date=item['Date'],
                Unique_squirrel_ID=item['Unique Squirrel ID'],
                Age=item['Age'],
                Primary_Fur_Color=item['Primary Fur Color'],
                Location=item['Location'],
                Specific_Location=item['Specific Location'],
                Running=strtobool(item['Running']),
                Chasing=strtobool(item['Chasing']),
                Climbing=strtobool(item['Climbing']),
                Fur_Color = (item['Highlight Fur Color'])
                Eating=strtobool(item['Eating']),
                Foraging=strtobool(item['Foraging']),
                Other_Activities=item['Other Activities'],
                Kuks=strtobool(item['Kuks']),
                Quaas=strtobool(item['Quaas']),
                Moans=strtobool(item['Moans']),
                Tail_flags=strtobool(item['Tail flags']),
                Tail_twitching=strtobool(item['Tail twitches']),
                Approaches=strtobool(item['Approaches']),
                Indifferent=strtobool(item['Indifferent']),
                Runs_from=strtobool(item['Runs from']),
            )
            s.save()
