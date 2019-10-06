import glog
import datetime
from utils import file_cache
from people import education, position, linkedin_base

class Profile(object):
    def __init__(self):
        self.fullName = None
        self.locationName = None
        self.num_positions = None
        self.num_educations = None

    def __repr__(self):
        return 'Profile <{}, {}, #positions: {}, #educations: {}>'.format(self.fullName, self.locationName, self.num_positions, self.num_educations)

    def from_linkedin(self, linkedin_dict):
        profile_linkedin = linkedin_dict['com.linkedin.voyager.dash.identity.profile.Profile'][0]
        self.fullName = profile_linkedin['firstName'] + ' ' + profile_linkedin['lastName']
        self.summary = profile_linkedin['summary']
        self.locationName = profile_linkedin['locationName']
        self.countryCode = profile_linkedin['location']['countryCode'].upper()
        self.num_positions = len(linkedin_dict['com.linkedin.voyager.dash.identity.profile.Position'])
        self.num_educations = len(linkedin_dict['com.linkedin.voyager.dash.identity.profile.Education'])
        self.positions = sorted([position.Position(exp) for exp in linkedin_dict['com.linkedin.voyager.dash.identity.profile.Position']], key=lambda x: x.rank_date, reverse=True)
        self.educations = sorted([education.Education(edu) for edu in linkedin_dict['com.linkedin.voyager.dash.identity.profile.Education']], key=lambda x: x.rank_date, reverse=True)

    def get_positions(self):
        return self.positions
    
    def get_educations(self):
        return self.educations

    def get_grad_date(self):
        grad_date = None
        if self.educations:
            grad_date = self.educations[0].end_date
        elif not grad_date and self.positions:
            grad_date = self.positions[-1].start_date
        return grad_date
              
    def get_experience_years(self):
        grad_date = self.get_grad_date()
        if grad_date:
            return (datetime.date.today() - grad_date).days/365
    
    def get_current_location(self):
        return self.locationName
    
    def get_current_title(self):
        if self.positions:
            return self.positions[0].get_title()

    def get_current_company(self):
        if self.positions:
            return self.positions[0].get_company_name()
    
    def get_highest_degree(self):
        if self.educations:
            return self.educations[0].get_degree()
    
    def get_skills(self):
        """based on TFIDF for descriptions"""
        pass
    
    def get_projects(self):
        pass
    
    def get_certificates(self):
        pass
    
    def get_spoken_langauges(self):
        pass
    
    def predict_profile_language(self):
        """ based on langid """
        pass

    def get_industry(self):
        pass

    def is_industry_changed(self):
        pass

if __name__ == '__main__':
    profile_obj = Profile()
    linkedin_dict = list(file_cache.cache['linkedin_profiles'].values())[0]
    profile_obj.from_linkedin(linkedin_dict)
    glog.info(profile_obj)
