
import datetime
from models import geocode

class LinkedinBase(object):
    def __init__(self):
        self.start_date = None
        self.end_date = None

    def translate_date_range(self, date_range_linkedin):
        self.start_date = self.translate_date(date_range_linkedin.get('start', {}))
        self.end_date = self.translate_date(date_range_linkedin.get('end', {}))
        if self.end_date:
            self.rank_date = self.end_date
        elif self.start_date:
            self.rank_date = self.start_date
        else:
            self.rank_date = datetime.date.today()       

    def translate_date(self, date_linkedin):
        year = date_linkedin.get('year') if date_linkedin else None
        if year:
            return datetime.date(year, date_linkedin.get('month', 1), date_linkedin.get('day', 1))

    def get_start_date(self):
        return self.start_date
    
    def get_end_date(self):
        return self.end_date

    def get_duration(self):
        if self.start_date and self.end_date:
            return (self.end_date - self.start_date).days

    def lookup_location(self, token):
        return geocode.lookup(token)
