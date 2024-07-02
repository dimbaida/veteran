from django.core.management.base import BaseCommand
from electricity.models import Plot, Measurement
import csv
from pathlib import Path


class Command(BaseCommand):
    help = 'Create a number of Plot models from a predefined list'

    @staticmethod
    def readValues():
        filepath = Path(__file__).parent / 'plots.csv'
        with open(filepath, mode='r') as csv_file:
            table = csv.reader(csv_file)
            return list(table)

    def handle(self, *args, **kwargs):
        table = self.readValues()
        for row in table:
            verbose = row[0]
            value_night = row[2]
            value_day = row[3]
            value_night_avg = row[4]
            value_day_avg = row[5]
            print(f"plot {verbose}, val_day: {value_day}, val_night: {value_night}, val_day_avg: {value_day_avg}, val_night_avg: {value_night_avg}")
            plot, plot_created = Plot.objects.get_or_create(verbose=verbose,
                                                            value_night_avg=value_night_avg,
                                                            value_day_avg=value_day_avg)
            if plot_created:
                print(plot, 'created')
                measurement, measurement_created = Measurement.objects.get_or_create(value_day=value_day,
                                                                                     value_night=value_night,
                                                                                     plot=plot,
                                                                                     user_id=1,
                                                                                     comment='Покази на момент запуску сайту')
                if measurement_created:
                    print(measurement, 'ctreated')
            else:
                print(plot, 'failed')
            print('----')
