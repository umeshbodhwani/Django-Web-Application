from django.core.management.base import BaseCommand

import csv
  
from squirrel_tracker.models import Squirrel

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')
    def handle(self, *args, **options):
        dict_ = {}
        sq = Squirrel.objects.all()
        with open(options['csv_file'],"w") as f:
            for item in sq:
                dict_['X'] = item.X
                dict_['Y'] = item.Y
                dict_['Shift'] = item.Shift
                dict_['Date'] = item.Date
                dict_['Unique Squirrel ID'] = item.Unique_squirrel_ID
                dict_['Age'] = item.Age
                dict_['Primary Fur Color'] = item.Primary_Fur_Color
                dict_['Location'] = item.Location
                dict_['Specific Location'] = item.Specific_Location
                dict_['Running'] = item.Running
                dict_['Chasing'] = item.Chasing
                dict_['Climbing'] = item.Climbing
                dict_['Eating'] = item.Eating
                dict_['Foraging'] = item.Foraging
                dict_['Other Activities'] = item.Other_Activities
                dict_['Kuks'] = item.Kuks
                dict_['Quaas'] = item.Quaas
                dict_['Moans'] = item.Moans
                dict_['Tail Flags'] = item.Tail_flags
                dict_['Tail Twitches'] = item.Tail_twitching
                dict_['Approaches'] = item.Approaches
                dict_['Indifferent'] = item.Indifferent
                dict_['Runs from'] = item.Runs_from
                writer = csv.DictWriter(f,delimiter=",",fieldnames=dict_.keys())
                writer.writeheader()
                writer.writerow(dict_)
