from people import linkedin_base

class Position(linkedin_base.LinkedinBase):
    def __init__(self, position_linkedin):
        self.companyName = position_linkedin['companyName']
        self.description = position_linkedin['description']
        self.locationName = position_linkedin['locationName']
        self.title = position_linkedin['title']
        self.translate_date_range(position_linkedin['dateRange'])
        self.duration = self.get_duration()

    def __repr__(self):
        return 'Position <{}, {}, {} to {}>'.format(self.title, self.companyName, self.start_date, self.end_date)

    def get_company_name(self):
        return self.companyName

    def get_title(self):
        return self.title

    def get_location(self):
        return self.locationName

    def predict_seniority(self):
        """ inferred from title name """
        pass
    
    def predict_industry(self):
        """ based on Wikipedia text for the company"""
        pass

    def predict_company_ranking(self):
        """ get from crunchbase https://pypi.org/project/python-crunchbase/ """
        pass