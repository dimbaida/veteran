from django.core.management.base import BaseCommand
from electricity.models import Plot, Measurement
import pandas as pd
import numpy as np
from pathlib import Path


class Command(BaseCommand):
    help = 'Create a number of Plot models from a predefined list'

    def readValues(self):
        filepath = Path(__file__).parent / 'plots.csv'
        df = pd.read_csv(filepath)
        return df

    def handle(self, *args, **kwargs):
        table = self.readValues()
        for i in range(0, table.shape[0]):
            verbose = table.loc[i, 'verbose']
            value_night = table.loc[i, 'value_night']
            if np.isnan(value_night):
                value_night = None
            value_day = table.loc[i, 'value_day']
            plot, created = Plot.objects.get_or_create(verbose=verbose)
            if created:
                print(plot, 'created')
                measurement, success = Measurement.objects.get_or_create(value_night=value_night,
                                                                         value_day=value_day,
                                                                         plot=plot,
                                                                         user_id=1,
                                                                         comment='Показ на момент запуску сайту')
                if success:
                    print(measurement, 'ctreated')
            else:
                print(plot, 'failed')
            print('----')
