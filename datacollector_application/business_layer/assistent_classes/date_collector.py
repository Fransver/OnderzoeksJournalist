import datetime
import pandas as pd


class DateCollector:

    def get_range_of_dates(self, starting_date, end_date=datetime.date.today()):
        return pd.date_range(starting_date, end_date).tolist()