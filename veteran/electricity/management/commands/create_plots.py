from django.core.management.base import BaseCommand
from electricity.models import Plot, Measurement
import csv
from pathlib import Path


class Command(BaseCommand):
    help = 'Create a number of Plot models from a predefined list'

    def readValues(self):
        filepath = Path(__file__).parent / 'plots.csv'
        with open(filepath, mode='r') as csv_file:
            table = csv.reader(csv_file)
            return list(table)

    def handle(self, *args, **kwargs):
        table = self.readValues()
        for row in table:
            verbose = row[0]
            value_day = row[3]
            value_night = row[2]
            print(verbose, value_day, value_night)
            plot, plot_created = Plot.objects.get_or_create(verbose=verbose)
            if created:
                print(plot, 'created')
                measurement, measurement_created = Measurement.objects.get_or_create(value_day=value_day,
                                                                         value_night=value_night,
                                                                         plot=plot,
                                                                         user_id=1,
                                                                         comment='Показ на момент запуску сайту')
                if measurement_created:
                    print(measurement, 'ctreated')
            else:
                print(plot, 'failed')
            print('----')
