import datetime


class DateCollector:

    @staticmethod
    def get_range_of_dates(starting_date, end_date=datetime.date.today()):
        return [starting_date + datetime.timedelta(days=x) for x in range((end_date-starting_date).days + 1)]
